from pyasn1.type import namedtype, tag, univ
from pyasn1.codec.der import decoder as der_decoder
from pyasn1.codec.der import encoder as der_encoder


class DSAPublicKey(univ.Integer):
    def get_bits(self):
        return len('{:x}'.format(self._value) * 4)

    def get_info(self):
        key_info = dict(
            bits=self.get_bits(),
            type='DSA',
            data=der_encoder.encode(self),
            pub=self.get_pub(),
        )
        if hasattr(self, 'parameters'):
            key_info.update(self.parameters.get_info())
        return key_info

    def get_pub(self):
        return self._value

    def get_p(self):
        if self.parameters:
            return self.parameters.get_p()
        else:
            return 0

    def get_q(self):
        if self.parameters:
            return self.parameters.get_q()
        else:
            return 0

    def get_g(self):
        if self.parameters:
            return self.parameters.get_g()
        else:
            return 0

    def set_parameters(self, der_parameters):
        self.parameters, _ = der_decoder.decode(
            der_parameters,
            asn1Spec=DSSParms()
        )
        return self


class DSSParms(univ.Sequence):
    '''
    Dss-Parms  ::=  SEQUENCE  {
            p       OCTET STRING,
            q       OCTET STRING,
            g       OCTET STRING  }
    '''
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('p', univ.Integer()),
        namedtype.NamedType('q', univ.Integer()),
        namedtype.NamedType('g', univ.Integer()),
    )

    def get_p(self):
        return self.getComponentByName('p')._value

    def get_q(self):
        return self.getComponentByName('q')._value

    def get_g(self):
        return self.getComponentByName('g')._value
