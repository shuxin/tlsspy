import os
import random


def exp(x, n, m):
    '''
    Calculate :math:`x^n \mod m`.
    '''
    y = 1
    z = x
    while n > 0:
        if n & 1:
            y = (y * z) % m
        z = (z * z) % m
        n //= 2
    return y


def is_prime(n, k):
    '''
    Checks whether ``n`` is probably a prime using the Miller-Rabin test, has
    a probability of :math:`1 - 4^(-k)`.
    '''

    if n % 2 == 0:
        return False

    d = n - 1
    s = 0

    while d % 2 == 0:
        s += 1
        d /= 2

    for i in xrange(k):
        a = long(2 + random.randint(0, n - 4))
        x = exp(a, d, n)
        if x == 1 or x == (n - 1):
            continue

        for r in xrange(1, s):
            x = (x * x) % n
            if x == 1:
                return False
            if x == n - 1:
                break

    return True


def get_prime(size, accuracy):
    '''
    Generate a pseudo random prime number with the specified size (in bytes).
    '''
    while True:
        rstr = os.urandom(size - 1)
        r = 128 | ord(os.urandom(1))
        for c in rstr:
            r = (r << 8) | ord(c)
        r |= 1

        if is_prime(r, accuracy):
            return r


def get_prime_upto(n, accuracy):
    '''
    Find the largest prime less than ``n``.
    '''
    n |= 1
    while n > 0:
        n -= 2
        if is_prime(n, accuracy):
            return n
