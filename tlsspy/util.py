from collections import OrderedDict, MutableSet
import datetime
import os
import Queue
import string
import threading

from pyasn1.codec.der import decoder as der_decoder
from pyasn1.type import char, univ

from tlsspy.asn1_models import x509
from tlsspy.log import log
from tlsspy.oids import friendly_oid

try:
    if 'SKIP_GMPY' in os.environ:
        raise ImportError()
    import gmpy
    has_gmpy = True
except ImportError:
    log.warning('Could not load gmpy, calculations may be slow(er)')
    has_gmpy = False


ASN1_GENERALIZEDTIME = (
    r'%Y%m%d%H%M%SZ',
    r'%Y%m%d%H%M%S%z',
)


def merge(a, b):
    '''Recursively merge two dictionaries.'''
    for key in set(a.keys()).union(b.keys()):
        if key in a and key in b:
            yield (key, dict(merge(a[key], b[key])))
        elif key in a:
            yield (key, a[key])
        else:
            yield (key, b[key])


def get_random_bytes(size):
    '''
    Get ``size`` of random bytes.
    '''
    b = bytearray(os.urandom(size))
    assert len(b) == size
    return b


def pad_hex(value, pad_size=2, separator=':'):
    '''
    Hexadecimal representation of a number with added padding.

    >>> print pad_hex(1234)
    04:d2
    >>> print pad_hex(12345)
    30:39
    >>> print pad_hex(12345678901234567890, pad_size=4)
    ab54:a98c:eb1f:0ad2
    '''
    encoded = '{0:x}'.format(value)
    while len(encoded) % pad_size > 0:
        encoded = '0{}'.format(encoded)

    return ':'.join(encoded[i:i + pad_size]
                    for i in xrange(0, len(encoded), pad_size))

def pad_binary(value):
    encoded = []
    for char in value:
        encoded.append(char if char in string.printable else '.')
    return ''.join(encoded)


class OrderedSet(MutableSet):
    '''
    Set that remembers the original insertion order.
    '''

    def __init__(self, iterable=None):
        self.end = end = []
        end += [None, end, end]  # sentinel
        self.map = {}

        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            cur = end[1]
            cur[2] = end[1] = self.map[key] = [key, cur, end]

    def discard(self, key):
        if key in self.map:
            key, prv, nxt = self.map.pop(key)
            prv[2] = nxt
            nxt[1] = prv

    def __iter__(self):
        end = self.end
        cur = end[2]
        while cur is not end:
            yield cur[0]
            cur = cur[2]

    def __reversed__(self):
        end = self.end
        cur = end[1]
        while cur is not end:
            yield cur[0]
            cur = cur[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('Empty set')

        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        else:
            return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        else:
            return set(self) == set(other)


class ThreadPoolDone(object):
    '''
    Sentinel object for the :class:`ThreadPool` workers to notify they are
    done processing.
    '''
    pass


class ThreadPool(object):
    '''
    Pool of threaded workers.
    '''

    Done = ThreadPoolDone

    def __init__(self):
        self._active_threads = 0
        self._jobs           = Queue.Queue()
        self._results        = Queue.Queue()
        self._threads        = []

    def add_job(self, func, args):
        '''
        Queue a new function for processing by a worker.

        :arg func: callable function
        :arg args: tuple of arguments
        '''
        self._jobs.put((func, args))

    def get_results(self):
        '''
        Generator function returning all the results from the workers until
        they are done processing.
        '''
        active_threads = self._active_threads
        while active_threads or not self._results.empty():
            result = self._results.get()
            if isinstance(result, ThreadPool.Done):
                active_threads -= 1
                self._results.task_done()
                continue

            else:
                self._results.task_done()
                yield result

    def join(self):
        '''
        Wait for all the workers to finish.
        '''
        self._jobs.join()
        self._active_threads = 0
        self._results.join()

    def start(self, workers):
        '''
        Start workers in the thread pool.

        :arg workers: number of workers
        '''
        log.info('Starting {0} thread pool workers'.format(workers))
        if self._active_threads:
            raise SyntaxError('Already started')

        for x in xrange(workers):
            worker = threading.Thread(
                target=self._work,
                args=(self._jobs, self._results),
                name='worker_{:03d}'.format(x),
            )
            worker.start()
            self._threads.append(worker)
            self._active_threads += 1

        for worker in self._threads:
            self._jobs.put(ThreadPool.Done())

        log.info('Done starting workers')

    def _work(self, jobs, results):
        while True:
            job = jobs.get()

            if isinstance(job, ThreadPool.Done):
                log.debug('[{0}] done'.format(
                    threading.currentThread().name,
                ))
                # Bye!
                results.put(ThreadPool.Done())
                jobs.task_done()
                break

            func = job[0]
            args = job[1]
            try:
                result = func(*args)
            except Exception as error:
                log.error('Uncaught exception in thread worker: {0}'.format(
                    error,
                ))
            else:
                results.put(result)
            finally:
                jobs.task_done()
