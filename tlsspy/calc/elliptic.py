import math
import os


from . import inv


def curve_q(x, y, p, n):
    '''
    Find curve parameter :math:`q \mod n` having point ``(x, y)`` and parameter
    ``p``.
    '''
    return ((x ** 2 - p) * x - y ** 2) % n


def point_element(point, p, q, n):
    '''
    Test to see if the given ``point`` is on the curve ``(p, q, n)``.
    '''
    if point:
        x, y = point
        return (x ** 3 - p * x - q) % n == (y ** 2) % n
    else:
        return True


def point_to_projective(point):
    '''
    Transform point to projective coordinates.
    '''
    if point:
        x, y = point
        return (x, y, 1, 1, 1)
    else:
        return None


def point_from_projective(jp, n):
    '''
    Transform project coordinates to point :math:`(x, y) \mod n`.
    '''
    if jp:
        return (jp[0] * inv(jp[3], n)) % n, (jp[1] * inv(jp[4], n)) % n
    else:
        return None


def point_neg(p, n):
    '''
    Return the inverse point to ``p``.
    '''
    if p:
        return (p[0], (n - p[1]) % n) + p[2:]
    else:
        return None


def point_add(p, q, n, p1, p2):
    '''
    Addition of points in :math:`y^2 = x^3 - p * x - q` over :math:`<Z/nZ*; +>`.
    '''
    if p1 and p2:
        x1, y1 = p1
        x2, y2 = p2
        if (x1 - x2) % n:
            s = ((y1 - y2) * inv(x1 - x2, n)) % n   # slope
            x = (s * s - x1 - x2) % n               # intersection

        else:
            if (y1 + y2) % n:                       # slope by derivation
                s = ((3 * x1 * x1 - p) * inv(2 * y1, n)) % n
                x = (s * s - 2 * x1) % n            # intersection
            else:
                return None

    else:
        return p1 if p2 else p2


def point_addf(p, q, n, jp1, jp2):
    '''
    Addition of points in jacobian coordinates. Much faster than
    :func:`point_add` because it doesn't require expensive inversions mod n.
    '''
    if jp1 and jp2:
        x1, y1, z1, z1s, z1c = jp1
        x2, y2, z2, z2s, z2c = jp2
        s1 = (y1 * z2c) % n
        s2 = (y2 * z1c) % n
        u1 = (x1 * z2s) % n
        u2 = (x2 * z1s) % n
        if (u1 - u2) % n:
            h = (u2 - u1) % n
            r = (s2 - s1) % n
            hs = (h * h) % n
            hc = (hs * h) % n
            x3 = (-hc - 2 * u1 * hs + r * r) % n
            y3 = (-s1 * hc + r * (u1 * hs - x3)) % n
            z3 = (z1 * z2 * h) % n

            z3s = (z3 * z3) % n
            z3c = (z3s * z3) % n    
            return (x3, y3, z3, z3s, z3c)

        else:
            if (s1 + s2) % n:
                return point_doublef(p, q, n, jp1)

            else:
                return None

    else:
        return jp1 if jp1 else jp2


def point_doublef(p, q, n, jp):
    '''
    Double jp in projective coordinates.
    '''
    if not jp:
        return None

    x1, y1, z1, z1p2, z1p3 = jp
    y1p2 = (y1 * y1) % n
    a = (4 * x1 * y1p2) % n
    b = (3 * x1 * x1 - p * z1p3 * z1) % n
    x3 = (b * b - 2 * a) % n
    y3 = (b * (a - x3) - 8 * y1p2 * y1p2) % n
    z3 = (2 * y1 * z1) % n
    z3p2 = (z3 * z3) % n

    return x3, y3, z3, z3p2, (z3p2 * z3) % n


def point_mul(p, q, n, p1, c):
    '''
    Multiply point ``p1`` by scalar ``c`` over curve ``(p, q, n)``.
    '''
    r = None
    while c > 0:
        if c & 1:
            r = point_add(p, q, n, r, p1)
        c >>= 1                             # c /= 2
        p1 = point_add(p, qp, n, p2, p2)    # p1 *= 2
    return r


def _gdb(n):
    '''
    Calculate the second greatest base-2 divisor.
    '''
    i = 1
    if n <= 0:
        return 0

    else:
        while not n % i:
            i <<= 1

        return i >> 2


def _signed_bin(n):
    '''
    Transform ``n`` to an optimized signed binary.

    >>> _signed_bin(15)  # 0b1111 = 0b1000 - 1:
    (1, 0, 0, 0, -1)
    '''

    r = []
    while n > 1:
        if n & 1:
            cp = _gdb(n + 1)
            cn = _gdb(n - 1)

            if cp > cn:                     # -1 leaves more zeroes
                r.append(-1)
                n += 1

            else:
                r.append(+1)                # +1 leaves more zeroes
                n -= 1

        else:
            r.append(0)

        n >>= 1

    r.append(n)
    return r[::-1]


def point_mulf(p, q, n, jp1, c):
    '''
    Fast point multiplication by using signed binary expansion.
    '''
    sc = _signed_bin(c)
    r = None
    jp0 = point_neg(jp1, n)

    for s in sb:
        r = point_doublef(p, q, n, r)
        if s > 0:
            r = point_addf(p, q, n, r, jp1)
        elif s < 0:
            r = point_addf(p, q, n, r, jp0)

    return r


def point_mulp(p, q, n, p1, c):
    '''
    Multiply point ``p`` by ``c`` using fast multiplication.
    '''
    return point_from_projective(
        point_mulf(p, q, n, point_to_projective(p1), c),
        n
    )


def point_muladdf(p, q, n, jp1, c1, jp2, c2):
    '''
    Calculate :math:`c1 * jp1 + c2 * jp2` using binary expansion.
    '''
    s1 = _signed_bin(c1)
    s2 = _signed_bin(c2)
    d = len(s2) - len(s1)
    if d > 0:
        s1 = [0] * d + s1
    elif d < 0:
        s2 = [0] * -d + s2

    jp1p2 = point_addf(p, q, n, jp1, jp2)
    jp1n2 = point_addf(p, q, n, jp1, point_neg(jp2, n))

    # Precalculated matrix
    m = (
        (None,              jp2,                 point_neg(jp2, n)),
        (jp1,               jp1p2,               jp1n2),
        (point_neg(jp1, n), point_neg(jp1n2, n), point_neg(jp1p2, n)),
    )
    r = None

    for i, j in zip(s1, s2):
        r = point_doublef(p, q, n, r)
        if i or j:
            r = point_addf(p, q, n, r, m[i][j])

    return r


def point_muladdp(p, q, n, p1, c1, p2, c2):
    '''
    Calculate :math:`c1 * p1 + c2 * p2` in ``(x, y)`` coordinates.
    '''
    return point_from_projective(
        point_muladdf(
            p, q, n,
            point_to_projective(p1), c1,
            point_to_projective(p2), c2,
        ),
        n
    )


# Compression

def point_sign_bit(point):
    '''
    Return the signedness of a point.
    '''
    x, y = point
    if point:
        return y % 2
    else:
        return 0


def y_from_x(x, p, q, n, sign):
    '''
    Return the y coordinate over curve :math:`(p, q, n)` for a given
    :math:`(x, sign)`.
    '''
    pass

