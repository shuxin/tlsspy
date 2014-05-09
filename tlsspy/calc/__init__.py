import math
import os

from tlsspy.log import log


try:
    if 'SKIP_GMPY' in os.environ:
        raise ImportError()
    import gmpy
    has_gmpy = True
except ImportError:
    log.warning('Could not load gmpy, calculations may be slow(er)')
    has_gmpy = False


# Number/byte conversions

def bytes_to_long(b):
    '''
    Convert a byte sequence to its long value.

    >>> bytes_to_long('\x42\x2a')
    16938L
    '''
    total = 0L
    multi = 1L
    for count in range(len(b) - 1, -1, -1):
        value = b[count]
        total += multi * value
        multi <<= 8
    return total


def long_to_bytes(n, limit=None):
    '''
    Convert a long value to a byte sequence in big endian.

    >>> long_to_bytes(16938)
    bytearray('B*')
    >>> long_to_bytes(16938, 1)
    bytearray('*')
    '''
    if limit == None:
        limit = num_bytes(n)

    b = bytearray(limit)
    for count in range(limit - 1, -1, -1):
        b[count] = int(n % 256)
        n >>= 8
    return b


def num_bits(n):
    r'''
    Returns the number of bits used to generated number ``n``. Calculates:

    .. math::
        \log(n, 2) - 1
    '''
    if n == 0:
        return 0
    else:
        s = '{0:x}'.format(n)
        return ((len(s) - 1) * 4) + {
            '0': 0, '1': 1, '2': 2, '3': 2,
            '4': 3, '5': 3, '6': 3, '7': 3,
        }.get(s[0], 4)


def num_bytes(n):
    r'''
    Returns the number of bytes used to generate number ``n``. Calculates:

    .. math::
        \providecommand{\ceil}[1]{\left \lceil #1 \right \rceil }
        \ceil{(log(n, 2) - 1)/8}
    '''
    if n == 0:
        return 0
    else:
        bits = num_bits(n)
        return int(math.ceil(bits / 8.0))


# Basic math


def curve_q(x, y, p, n):
    '''
    Find curve parameter :math:`q \mod n` having point ``(x, y)`` and parameter
    ``p``.
    '''
    return ((x ** 2 - p) * x - y ** 2) % n


def element(point, p, q, n):
    '''
    Test to see if the given ``point`` is on the curve ``(p, q, n)``.
    '''
    if point:
        x, y = point
        return (x ** 3 - p * x - q) % n == (y ** 2) % n
    else:
        return True


def euclid(a, b):
    '''
    Solve :math:`x * a + y * b = \ggt(a, b)` and return
    :math:`(x, y, \ggt(a, b))`.
    '''
    x = yy = 0
    y = xx = 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx - q * x, x
        y, yy = yy - q * y, y
    return xx, yy, a


def inv(a, n):
    '''
    Returns inversion :math:`1/a \mod n` where ``a`` and ``n`` should be
    co primes.
    '''
    i = euclid(a, n)[0]
    while i < 0:
        i += n
    return i


def inv_mod(a, b):
    '''
    Inverse of :math:`a \mod b` using the Extended Euclidean Algorithm:

    .. math::
        ax + by = \gcd(a, b)
    '''
    c, d = a, b
    uc, ud = 1, 0

    while c != 0:
        q = d // c
        c, d = d - (q * c), c
        uc, ud = ud - (q * uc), uc

    if d == 1:
        return ud % b
    else:
        return 0


def pow_mod(b, p, m):
    '''
    Power with modulus.

    :arg b: base
    :arg p: power
    :arg m: modulus

    For :math:`p < 0`:

    .. math::
        (b^p \mod m) \pmod m

    For :math:`p >= 0`:

    .. math::
        b^p \mod m
    '''
    if has_gmpy:
        b = gmpy.mpz(b)
        p = gmpy.mpz(p)
        m = gmpy.mpz(m)
        return long(pow(b, p, m))

    elif p < 0:
        return inv_mod(pow(b, p, m), m)

    else:
        return pow(b, p, m)
