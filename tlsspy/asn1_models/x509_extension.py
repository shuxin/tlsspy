from pyasn1.type import (
    char,
    constraint,
    namedtype,
    namedval,
    tag,
    univ,
    useful,
)

from tlsspy.asn1_models.generic import ConvertableBitString
from tlsspy.asn1_models.x509 import (
    id_qt_cps,
    id_qt_unotice,
    AlgorithmIdentifier,
    CertificateSerialNumber,
    DirectoryString,
    Extensions,
    GeneralName,
    GeneralNames,
    MAX,
    Name,
    OptionalValidity,
    RelativeDistinguishedName,
    SubjectPublicKeyInfo,
    UniqueIdentifier,
    Version,
)
from tlsspy.oids import friendly_oid
from tlsspy.parser import extension, generic


class AccessDescription(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('accessMethod', univ.ObjectIdentifier()),
        namedtype.NamedType('accessLocation', GeneralName())
    )


class AuthorityInfoAccess(univ.SequenceOf):
    componentType = AccessDescription()
    to_python = extension.parse_authority_info_access
    subtypeSpec = univ.SequenceOf.subtypeSpec + constraint.ValueSizeConstraint(
        1, MAX
    )


class KeyPurposeId(univ.ObjectIdentifier):
    pass


class ExtKeyUsageSyntax(univ.SequenceOf):
    componentType = KeyPurposeId()
    to_python = extension.parse_ext_key_usage
    subtypeSpec = univ.SequenceOf.subtypeSpec + constraint.ValueSizeConstraint(
        1, MAX
    )


class AnyQualifier(univ.Choice):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('userNotice', univ.Sequence()),
        namedtype.NamedType('cpsUri', char.IA5String()),
    )


class PolicyQualifierId(univ.ObjectIdentifier):
    subtypeSpec = univ.ObjectIdentifier.subtypeSpec + constraint.SingleValueConstraint(
        id_qt_cps, id_qt_unotice
    )


class CertPolicyId(univ.ObjectIdentifier):
    pass


class PolicyQualifierInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('policyQualifierId', PolicyQualifierId()),
        namedtype.NamedType('qualifier', AnyQualifier()),
    )


class PolicyQualifiers(univ.SequenceOf):
    componentType = PolicyQualifierInfo()


class PolicyInformation(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('policyIdentifier', univ.ObjectIdentifier()),
        namedtype.OptionalNamedType('policyQualifiers', PolicyQualifiers()),
    )
    to_python = extension.parse_policy_information


class CertificatePolicies(univ.SequenceOf):
    componentType = PolicyInformation()
    to_python = generic.parse_sequence_list
    #subtypeSpec = univ.SequenceOf.subtypeSpec + constraint.ValueSizeConstraint(
    #    1, MAX
    #)


class KeyUsage(univ.BitString):
    namedValues = namedval.NamedValues(
        ('digitalSignature', 0),
        ('nonRepudiation', 1),
        ('keyEncipherment', 2),
        ('dataEncipherment', 3),
        ('keyAgreement', 4),
        ('keyCertSign', 5),
        ('cRLSign', 6),
        ('encipherOnly', 7),
        ('decipherOnly', 8),
    )
    to_python = extension.parse_key_usage


class KeyIdentifier(univ.OctetString):
    to_python = generic.parse_hex


class SubjectKeyIdentifier(KeyIdentifier):
    pass


class AuthorityKeyIdentifier(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.OptionalNamedType(
            'keyIdentifier', 
            KeyIdentifier().subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
            )
        ),
        namedtype.OptionalNamedType(
            'authorityCertIssuer', 
            GeneralNames().subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)
            )
        ),
        namedtype.OptionalNamedType(
            'authorityCertSerialNumber', 
            CertificateSerialNumber().subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
            )
        )
    )
    to_python = extension.parse_authority_key_identifier


class BasicConstraints(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.OptionalNamedType('cA', univ.Boolean(False)),
        namedtype.OptionalNamedType(
            'pathLenConstraint',
            univ.Integer().subtype(
                subtypeSpec=constraint.ValueRangeConstraint(0, MAX)
            )
        ),
    )
    to_python = extension.parse_basic_constraints


class CertificateIssuer(GeneralNames):
    pass


class ReasonFlags(univ.BitString):
    namedValues = namedval.NamedValues(
        ('unused', 0),
        ('keyCompromise', 1),
        ('cACompromise', 2),
        ('affiliationChanged', 3),
        ('superseded', 4),
        ('cessationOfOperation', 5),
        ('certificateHold', 6)
    )


class DistributionPointName(univ.Choice):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType(
            'fullName', 
            GeneralNames().subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        ),
        namedtype.NamedType(
            'nameRelativeToCRLIssuer', 
            RelativeDistinguishedName().subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
    to_python = generic.parse_choice


class DistributionPoint(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.OptionalNamedType(
            'distributionPoint', 
            DistributionPointName().subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        ),
        namedtype.OptionalNamedType(
            'reasons', 
            ReasonFlags().subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)
            )
        ),
        namedtype.OptionalNamedType(
            'cRLIssuer', 
            GeneralNames().subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    )
    to_python = extension.parse_distribution_point


class CRLDistributionPoints(univ.SequenceOf):
    componentType = DistributionPoint()
    subtypeSpec = univ.SequenceOf.subtypeSpec + constraint.ValueSizeConstraint(
        1, MAX
    )
    to_python = generic.parse_sequence_list


class SubjectAltName(GeneralNames):
    pass


class IssuerAltName(GeneralNames):
    pass


class NetscapeCertType(univ.BitString):
    to_python = extension.parse_netscape_cert_type


class NetscapeComment(DirectoryString):
    pass


class IA5StringSequence(univ.SequenceOf):
    componentType = char.IA5String()


class HashAlgAndValue(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('hashAlg', AlgorithmIdentifier()),
        namedtype.NamedType('hashValue', univ.OctetString()),
    )


class LogotypeDetails(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('mediaType', char.IA5String()),
        namedtype.NamedType('logotypeHash', HashAlgAndValue()),
        namedtype.NamedType('logotypeURI', IA5StringSequence())
    )


class LogotypeImageType(univ.Integer):
    namedValues = namedval.NamedValues(
        ('grayScale', 0),
        ('color', 1)
    )


class LogotypeImageResolution(univ.Choice):
    componentType = namedtype.NamedTypes(
        namedtype.DefaultedNamedType('numBits', univ.Integer()),
        namedtype.DefaultedNamedType('tableSize', univ.Integer())
    )


class LogotypeImageInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.DefaultedNamedType('type', LogotypeImageType('color')),
        namedtype.NamedType('fileSize', univ.Integer()),
        namedtype.NamedType('xSize', univ.Integer()),
        namedtype.NamedType('ySize', univ.Integer()),
        namedtype.OptionalNamedType('resolution', LogotypeImageResolution()),
        namedtype.OptionalNamedType('language', char.IA5String())
    )

class LogotypeImage(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType(
            'imageDetails',
            LogotypeDetails().subtype(
                explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
            )
        ),
        namedtype.OptionalNamedType(
            'imageInfo',
            LogotypeImageInfo().subtype(
                explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)
            )
        ),
    )


class LogotypeImageSequence(univ.SequenceOf):
    componentType = LogotypeImage()


class LogotypeAudioInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('fileSize', univ.Integer()),
        namedtype.NamedType('playTime', univ.Integer()),
        namedtype.NamedType('channels', univ.Integer()),
        namedtype.OptionalNamedType('sampleRate', univ.Integer()),
        namedtype.OptionalNamedType('language', char.IA5String())
    )


class LogotypeAudio(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType(
            'audioDetails',
            LogotypeDetails().subtype(
                explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
            )
        ),
        namedtype.OptionalNamedType(
            'audioInfo',
            LogotypeAudioInfo().subtype(
                explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)
            )
        )
    )


class LogotypeAudioSequence(univ.SequenceOf):
    componentType = LogotypeAudio()


class LogotypeData(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('image', LogotypeImageSequence()),
        namedtype.OptionalNamedType('audio', LogotypeAudioSequence())
    )


class LogotypeReference(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('refStructHash', HashAlgAndValue()),
        namedtype.NamedType('refStructURI', char.IA5String())
    )


class LogotypeInfo(univ.Choice):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType(
            'direct',
            LogotypeData().subtype(
                explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
            )
        ),
        namedtype.NamedType(
            'indirect',
            LogotypeReference().subtype(
                explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)
            )
        )
    )


class LogotypeInfoSequence(univ.SequenceOf):
    componentType = LogotypeInfo()


class OtherLogotypeInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('logotypeType', univ.ObjectIdentifier()),
        namedtype.NamedType('info', LogotypeInfo())
    )


class LogotypeExtn(univ.Sequence):
    componentType = namedtype.NamedTypes(
        # namedtype.OptionalNamedType(
        #     'communityLogos',
        #     LogotypeInfoSequence().subtype(
        #         explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
        #     )
        # ),
        namedtype.OptionalNamedType(
            'issuerLogo',
            LogotypeInfo().subtype(
                explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)
            )
        ),
        # namedtype.OptionalNamedType(
        #     'subjectLogo',
        #     LogotypeInfo().subtype(
        #         explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
        #     )
        # ),
        # namedtype.OptionalNamedType(
        #     'otherLogos',
        #     OtherLogotypeInfo().subtype(
        #         explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)
        #     )
        # ),
    )
