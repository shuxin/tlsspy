from pyasn1.type import namedtype, namedval, tag, univ

from tlsspy.calc import num_bytes, bytes_to_long
from tlsspy.crypto.named_curves import NAMED_CURVE
from tlsspy.log import log
from tlsspy.oids import friendly_oid

# RFC 5480 ECDSA signature identifiers
ANSI_X9_62_SIG        = '\x04'                          # signatures(4)
ANSI_X9_62_SIG_SHA2   = '\x03'                          # ecdsa-with-SHA2(3)
ECDSA_SHA1            = ANSI_X9_62_SIG + '\x01'         # ecdsa-with-SHA1
ECDSA_SHA224          = ANSI_X9_62_SIG_SHA2 + '\x01'    # ecdsa-with-SHA224
ECDSA_SHA256          = ANSI_X9_62_SIG_SHA2 + '\x02'    # ecdsa-with-SHA256
ECDSA_SHA384          = ANSI_X9_62_SIG_SHA2 + '\x03'    # ecdsa-with-SHA384
ECDSA_SHA512          = ANSI_X9_62_SIG_SHA2 + '\x04'    # ecdsa-with-SHA512

# http://cs.ucsb.edu/~koc/ccs130h/notes/ecdsa-cert.pdf


POINT_NULL         = (0x00,)
POINT_COMPRESSED   = (0x02, 0x03)
POINT_UNCOMPRESSED = (0x04,)


def parse_binary_point(blob, point_size):
    data = bytearray(blob)
    point_format = data[0]
    point_data = data[1:]
    if point_format in POINT_NULL:
        if len(point_data) == 0:
            return dict(x=1, y=1, z=0)
        else:
            raise ValueError()

    elif point_format in POINT_COMPRESSED:
        log.debug(
            'Parsing compressed point of {0} bytes with size {1}'.format(
                len(point_data),
                point_size,
            )
        )
        rest = point_data[point_size:]
        assert not rest, '{0} bytes remain in compressed binary point'.format(
            len(rest)
        )
        x = bytes_to_long(point_data[:point_size])
        y = x * ((point_format - 2) * -1)
        return dict(x=x, y=y, z=0)

    elif point_format in POINT_UNCOMPRESSED:
        log.debug(
            'Parsing uncompressed point of {0} bytes with size {1}'.format(
                len(point_data),
                point_size,
            )
        )
        rest = point_data[point_size + point_size:]
        assert not rest, '{0} bytes remain in binary point'.format(
            len(rest),
        )
        return dict(
            x=bytes_to_long(point_data[:point_size]),
            y=bytes_to_long(point_data[point_size:]),
            z=1,
        )

    else:
        raise ValueError('Unsupported point format {0:02x}'.format(
            data[0],
        ))


def parse_named_curve(named_curve):
    friendly = friendly_oid(named_curve)
    if friendly == named_curve:
        raise ValueError('No configuration for curve')
    else:
        return NAMED_CURVE[friendly]


class Curve(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('publicKeyType', univ.ObjectIdentifier()),
        namedtype.NamedType('curveName', univ.ObjectIdentifier()),
    )


class ECPoint(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('point', univ.OctetString()),
    )


class SpecifiedECDomainVersion(univ.Integer):
    namedValues = namedval.NamedValues(
        ('ecdpVer1', 1),
        ('ecdpVer2', 2),
        ('ecdpVer3', 3),
    )


class FieldID(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('fieldType', univ.OctetString()),
        namedtype.NamedType('parameters', univ.OctetString())
    )


class SpecifiedECDomain(univ.Sequence):
    '''
    Specified Domain Parameters, as per `SEC 1`_ C.2.


        SpecifiedECDomain ::= SEQUENCE {
            version SpecifiedECDomainVersion(ecdpVer1 | ecdpVer2 | ecdpVer3, ...),
            fieldID FieldID 44 FieldTypes 66 ,
            curve Curve,
            base ECPoint,
            order INTEGER,
            cofactor INTEGER OPTIONAL,
            hash HashAlgorithm OPTIONAL,
        }
    '''
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('version', SpecifiedECDomainVersion()),
        namedtype.NamedType('fieldID', FieldID()),
        namedtype.NamedType('curve', Curve()),
        namedtype.NamedType('base', ECPoint()),
        namedtype.NamedType('order', univ.Integer()),
        namedtype.OptionalNamedType('cofactor', univ.Integer()),
        #namedtype.OptionalNamedType('hash', HashAlgorithm()),
    )


class ECParameters(univ.Choice):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('namedCurve', univ.ObjectIdentifier()),
        namedtype.NamedType('specifiedCurve', SpecifiedECDomain()),
    )


class ECNamedCurve(object):
    def __init__(self, named_curve, key_data):
        log.debug('Parsing {0} ({1}) named curve'.format(
            friendly_oid(named_curve),
            named_curve,
        ))

        self.name = friendly_oid(named_curve)
        self.group = parse_named_curve(named_curve)
        self.point = parse_binary_point(key_data, self.group['point_size'])

    def get_bits(self):
        return self.group['size']

    def get_info(self):
        return dict(
            bits=self.get_bits(),
            type='EC',
            name=self.get_name(),
            point=self.get_point(),
        )

    def get_name(self):
        return self.name

    def get_point(self):
        return self.point
