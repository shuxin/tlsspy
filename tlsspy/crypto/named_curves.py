from tlsspy.calc import num_bytes


NAMED_CURVE = {}

# SEC2.2 - Recommended Elliptic Curve Domain Parameters over Fp

NAMED_CURVE['secp112r1'] = dict(
    p    = 0xdb7c2abf62e35e668076bead208bL,
    a    = 0xdb7c2abf62e35e668076bead208bL,
    b    = 0x659ef8ba043916eede8911702b22L,
    G    = 0x0409487239995a5ee76b55f9c2f098a89ce5af8724c0a23e0e0ff77500L,
    n    = 0xdb7c2abf62e35e7628dfac6561c5L,
    h    = 0x01,
    size = 112,
    bits = 56,
)

NAMED_CURVE['secp112r2'] = dict(
    p    = 0xdb7c2abf62e35e668076bead208bL,
    a    = 0x6127c24c05f38a0aaaf65c0ef02cL,
    b    = 0x51def1815db5ed74fcc34c85d709L,
    G    = 0x044ba30ab5e892b4e1649dd0928643adcd46f5882e3747def36e956e97L,
    n    = 0x36df0aafd8b8d7597ca10520d04bL,
    h    = 0x04,
    size = 112,
    bits = 56,
)

NAMED_CURVE['secp128r1'] = dict(
    p    = 0xfffffffdffffffffffffffffffffffffL,
    a    = 0xfffffffdfffffffffffffffffffffffcL,
    b    = 0xe87579c11079f43dd824993c2cee5ed3L,
    G    = 0x04161ff7528b899b2d0c28607ca52c5b86cf5ac8395bafeb13c02da292dded7a83L,
    n    = 0xfffffffe0000000075a30d1b9038a115L,
    h    = 0x01,
    size = 128,
    bits = 64,
)

NAMED_CURVE['secp128r2'] = dict(
    p    = 0xfffffffdffffffffffffffffffffffffL,
    a    = 0xd6031998d1b3bbfebf59cc9bbff9aee1L,
    b    = 0x5eeefca380d02919dc2c6558bb6d8a5dL,
    G    = 0x047b6aa5d85e572983e6fb32a7cdebc14027b6916a894d3aee7106fe805fc34b44L,
    n    = 0x3fffffff7fffffffbe0024720613b5a3L,
    h    = 0x04,
    size = 128,
    bits = 64,
)

NAMED_CURVE['secp160k1'] = dict(
    p    = 0xfffffffffffffffffffffffffffffffeffffac73L,
    a    = 0x0000000000000000000000000000000000000000L,
    b    = 0x0000000000000000000000000000000000000007L,
    G    = 0x043b4c382ce37aa192a4019e763036f4f5dd4d7ebb938cf935318fdced6bc28286531733c3f03c4feeL,
    n    = 0x0100000000000000000001b8fa16dfab9aca16b6b3L,
    h    = 0x01,
    size = 160,
    bits = 80,
)

NAMED_CURVE['secp160r1'] = dict(
    p    = 0xffffffffffffffffffffffffffffffff7fffffffL,
    a    = 0xffffffffffffffffffffffffffffffff7ffffffcL,
    b    = 0x1c97befc54bd7a8b65acf89f81d4d4adc565fa45L,
    G    = 0x044a96b5688ef573284664698968c38bb913cbfc8223a628553168947d59dcc912042351377ac5fb32L,
    n    = 0x0100000000000000000001f4c8f927aed3ca752257L,
    h    = 0x01,
    size = 160,
    bits = 80,
)

NAMED_CURVE['secp160r2'] = dict(
    p    = 0xfffffffffffffffffffffffffffffffeffffac73L,
    a    = 0xfffffffffffffffffffffffffffffffeffffac70L,
    b    = 0xb4e134d3fb59eb8bab57274904664d5af50388baL,
    G    = 0x0452dcb034293a117e1f4ff11b30f7199d3144ce6dfeaffef2e331f296e071fa0df9982cfea7d43f2eL,
    n    = 0x0100000000000000000000351ee786a818f3a1a16bL,
    h    = 0x01,
    size = 160,
    bits = 80,
)

NAMED_CURVE['secp192k1'] = dict(
    p    = 0xfffffffffffffffffffffffffffffffffffffffeffffee37L,
    a    = 0x000000000000000000000000000000000000000000000000L,
    b    = 0x000000000000000000000000000000000000000000000003L,
    G    = 0x04db4ff10ec057e9ae26b07d0280b7f4341da5d1b1eae06c7d9b2f2f6d9c5628a7844163d015be86344082aa88d95e2f9dL,
    n    = 0xfffffffffffffffffffffffe26f2fc170f69466a74defd8dL,
    h    = 0x01,
    size = 192,
    bits = 96,
)

NAMED_CURVE['secp192k2'] = dict(
    p    = 0xfffffffffffffffffffffffffffffffeffffffffffffffffL,
    a    = 0xfffffffffffffffffffffffffffffffefffffffffffffffcL,
    b    = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1L,
    G    = 0x04188da80eb03090f67cbf20eb43a18800f4ff0afd82ff101207192b95ffc8da78631011ed6b24cdd573f977a11e794811L,
    n    = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831L,
    h    = 0x01,
    size = 192,
    bits = 96,
)

NAMED_CURVE['secp224k1'] = dict(
    p    = 0xfffffffffffffffffffffffffffffffffffffffffffffffeffffe56dL,
    a    = 0x00000000000000000000000000000000000000000000000000000000L,
    b    = 0x00000000000000000000000000000000000000000000000000000005L,
    G    = 0x04a1455b334df099df30fc28a169a467e9e47075a90f7e650eb6b7a45c7e089fed7fba344282cafbd6f7e319f7c0b0bd59e2ca4bdb556d61a5L,
    n    = 0x010000000000000000000000000001dce8d2ec6184caf0a971769fb1f7L,
    h    = 0x01,
    size = 224,
    bits = 112,
)

NAMED_CURVE['secp224r1'] = dict(
    p    = 0xffffffffffffffffffffffffffffffff000000000000000000000001L,
    a    = 0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffeL,
    b    = 0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4L,
    G    = 0x04b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34L,
    n    = 0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3dL,
    h    = 0x01,
    size = 224,
    bits = 112,
)

NAMED_CURVE['secp256k1'] = dict(
    p    = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2fL,
    a    = 0x0000000000000000000000000000000000000000000000000000000000000000L,
    b    = 0x0000000000000000000000000000000000000000000000000000000000000007L,
    G    = 0x0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8L,
    n    = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141L,
    h    = 0x01,
    size = 256,
    bits = 128,
)

NAMED_CURVE['secp256r1'] = dict(
    p    = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffffL,
    a    = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffcL,
    b    = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604bL,
    G    = 0x046b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c2964fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5L,
    n    = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551L,
    h    = 0x01,
    size = 256,
    bits = 128,
)

NAMED_CURVE['secp384r1'] = dict(
    p    = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000ffffffffL,
    a    = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000fffffffcL,
    b    = 0xb3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aefL,
    G    = 0x04aa87ca22be8b05378eb1c71ef320ad746e1d3b628ba79b9859f741e082542a385502f25dbf55296c3a545e3872760ab73617de4a96262c6f5d9e98bf9292dc29f8f41dbd289a147ce9da3113b5f0b8c00a60b1ce1d7e819d7a431d7c90ea0e5fL,
    n    = 0xffffffffffffffffffffffffffffffffffffffffffffffffc7634d81f4372ddf581a0db248b0a77aecec196accc52973L,
    h    = 0x01,
    size = 384,
    bits = 192,
)

NAMED_CURVE['secp521r1'] = dict(
    p    = 0xffffffffffffffffffffffffffffffffffffffffffffffffc7634d81f4372ddf581a0db248b0a77aecec196accc52973L,
    a    = 0x01fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcL,
    b    = 0x0051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00L,
    G    = 0x0400c6858e06b70404e9cd9e3ecb662395b4429c648139053fb521f828af606b4d3dbaa14b5e77efe75928fe1dc127a2ffa8de3348b3c1856a429bf97e7e31c2e5bd66011839296a789a3bc0045c8a5fb42c7d1bd998f54449579b446817afbd17273e662c97ee72995ef42640c550b9013fad0761353c7086a272c24088be94769fd16650L,
    n    = 0x01fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffa51868783bf2f966b7fcc0148f709a5d03bb5c9b8899c47aebb6fb71e91386409L,
    h    = 0x01,
    size = 521,
    bits = 256,
)

# SEC2-3 Recommended Elliptic Curve Domain Parameters over F(2^m)

NAMED_CURVE['sect113r1'] = dict(
    f          = lambda x: x ** 113 + x ** 9 + 1,
    a          = 0x003088250ca6e7c7fe649ce85820f7L,
    b          = 0x00e8bee4d3e2260744188be0e9c723L,
    G          = 0x04009d73616f35f4ab1407d73562c10f00a52830277958ee84d1315ed31886L,
    n          = 0x0100000000000000d9ccec8a39e56fL,
    h          = 0x02,
    size       = 113,
    bits       = 56,
    point_size = 17,
)

NAMED_CURVE['sect113r2'] = dict(
    f          = lambda x: x ** 113 + x ** 9 + 1,
    a          = 0x00689918dbec7e5a0dd6dfc0aa55c7L,
    b          = 0x0095e9a9ec9b297bd4bf36e059184f,
    G          = 0x0401a57a6a7b26ca5ef52fcdb816479700b3adc94ed1fe674c06e695baba1dL,
    n          = 0x010000000000000108789b2496af93L,
    h          = 0x02,
    size       = 113,
    bits       = 56,
    point_size = 17,
)
NAMED_CURVE['sect131r1'] = dict(
    f          = lambda x: x ** 131 + x ** 8 + x ** 3 + x ** 2 + 1,
    a          = 0x07a11b09a76b562144418ff3ff8c2570b8L,
    b          = 0x0217c05610884b63b9c6c7291678f9d341L,
    G          = 0x040081baf91fdf9833c40f9c181343638399078c6e7ea38c001f73c8134b1b4ef9e150L,
    n          = 0x0400000000000000023123953a9464b54dL,
    h          = 0x02,
    size       = 131,
    bits   = 64,
    point_size = 17,
)

NAMED_CURVE['sect131r2'] = dict(
    f          = lambda x: x ** 131 + x ** 8 + x ** 3 + x ** 2 + 1,
    a          = 0x03e5a88919d7cafcbf415f07c2176573b2L,
    b          = 0x04b8266a46c55657ac734ce38f018f2192L,
    G          = 0x040356dcd8f2f95031ad652d23951bb366a80648f06d867940a5366d9e265de9eb240fL,
    n          = 0x0400000000000000016954a233049ba98fL,
    h          = 0x02,
    size       = 131,
    bits   = 64,
    point_size = 17,
)

NAMED_CURVE['sect163k1'] = dict(
    f          = lambda x: x ** 163 + x ** 7 + x ** 6 + x ** 3 + 1,
    a          = 0x000000000000000000000000000000000000000001L,
    b          = 0x000000000000000000000000000000000000000001L,
    G          = 0x0402fe13c0537bbc11acaa07d793de4e6d5e5c94eee80289070fb05d38ff58321f2e800536d538ccdaa3d9L,
    n          = 0x04000000000000000000020108a2e0cc0d99f8a5efL,
    h          = 0x02,
    size       = 163,
    bits   = 80,
    point_size = 21,
)

NAMED_CURVE['sect163r1'] = dict(
    f          = lambda x: x ** 163 + x ** 7 + x ** 6 + x ** 3 + 1,
    a          = 0x07b6882caaefa84f9554ff8428bd88e246d2782ae2L,
    b          = 0x0713612dcddcb40aab946bda29ca91f73af958afd9L,
    G          = 0x040369979697ab43897789566789567f787a7876a65400435edb42efafb2989d51fefce3c80988f41ff883L,
    n          = 0x03ffffffffffffffffffff48aab689c29ca710279bL,
    h          = 0x02,
    size       = 163,
    bits   = 80,
    point_size = 21,
)

NAMED_CURVE['sect163r2'] = dict(
    f          = lambda x: x ** 163 + x ** 7 + x ** 6 + x ** 3 + 1,
    a          = 0x000000000000000000000000000000000000000001L,
    b          = 0x020a601907b8c953ca1481eb10512f78744a3205fdL,
    G          = 0x0403f0eba16286a2d57ea0991168d4994637e8343e3600d51fbc6c71a0094fa2cdd545b11c5c0c797324f1L,
    n          = 0x040000000000000000000292fe77e70c12a4234c33L,
    h          = 0x02,
    size       = 163,
    bits       = 80,
    point_size = 21,
)

NAMED_CURVE['sect193r1'] = dict(
    f          = lambda x: x ** 193 + x ** 15 + 1,
    a          = 0x0017858feb7a98975169e171f77b4087de098ac8a911df7b01L,
    b          = 0x00fdfb49bfe6c3a89facadaa7a1e5bbc7cc1c2e5d831478814L,
    G          = 0x0401f481bc5f0ff84a74ad6cdf6fdef4bf6179625372d8c0c5e10025e399f2903712ccf3ea9e3a1ad17fb0b3201b6af7ce1b05L,
    n          = 0x01000000000000000000000000c7f34a778f443acc920eba49,
    h          = 0x02,
    size       = 193,
    bits       = 96,
    point_size = 25,
)

NAMED_CURVE['sect193r2'] = dict(
    f          = lambda x: x ** 193 + x ** 15 + 1,
    a          = 0x0163f35a5137c2ce3ea6ed8667190b0bc43ecd69977702709bL,
    b          = 0x00c9bb9e8927d4d64c377e2ab2856a5b16e3efb7f61d4316aeL,
    G          = 0x0400d9b67d192e0367c803f39e1a7e82ca14a651350aae617e8f01ce94335607c304ac29e7defbd9ca01f596f927224cdecf6cL,
    n          = 0x010000000000000000000000015aab561b005413ccd4ee99d5L,
    h          = 0x02,
    size       = 193,
    bits       = 96,
    point_size = 25,
)

NAMED_CURVE['sect233k1'] = dict(
    f=lambda x: x ** 233 + x ** 74 + 1,
    a=0x000000000000000000000000000000000000000000000000000000000000L,
    b=0x000000000000000000000000000000000000000000000000000000000001L,
    G=0x04017232ba853a7e731af129f22ff4149563a419c26bf50a4c9d6eefad612601db537dece819b7f70f555a67c427a8cd9bf18aeb9b56e0c11056fae6a3L,
    n=0x8000000000000000000000000000069d5bb915bcd46efb1ad5f173abdfL,
    h=0x04,
    size=223,
    bits=112,
    point_size=30,
)

NAMED_CURVE['sect233r1'] = dict(
    f          = lambda x: x ** 233 + x ** 74 + 1,
    a          = 0x000000000000000000000000000000000000000000000000000000000001L,
    b          = 0x0066647ede6c332c7f8c0923bb58213b333b20e9ce4281fe115f7d8f90adL,
    G          = 0x0400fac9dfcbac8313bb2139f1bb755fef65bc391f8b36f8f8eb7371fd558b01006a08a41903350678e58528bebf8a0beff867a7ca36716f7e01f81052L,
    n          = 0x01000000000000000000000000000013e974e72f8a6922031d2603cfe0d7L,
    h          = 0x02,
    size       = 233,
    bits       = 112,
    point_size = 30,
)

NAMED_CURVE['sect239k1'] = dict(
    f          = lambda x: x ** 239 + x ** 158 + 1,
    a          = 0x000000000000000000000000000000000000000000000000000000000000L,
    b          = 0x000000000000000000000000000000000000000000000000000000000001L,
    G          = 0x0429a0b6a887a983e9730988a68727a8b2d126c44cc2cc7b2a6555193035dc76310804f12e549bdb011c103089e73510acb275fc312a5dc6b76553f0caL,
    n          = 0x2000000000000000000000000000005a79fec67cb6e91f1c1da800e478a5L,
    h          = 0x04,
    size       = 239,
    bits       = 115,
    point_size = 30,
)

NAMED_CURVE['sect283k1'] = dict(
    f          = lambda x: x ** 283 + x ** 12 + x ** 7 + x ** 5 + 1,
    a          = 0x000000000000000000000000000000000000000000000000000000000000000000000000L,
    b          = 0x000000000000000000000000000000000000000000000000000000000000000000000001L,
    G          = 0x040503213f78ca44883f1a3b8162f188e553cd265f23c1567a16876913b0c2ac245849283601ccda380f1c9e318d90f95d07e5426fe87e45c0e8184698e45962364e34116177dd2259L,
    n          = 0x01ffffffffffffffffffffffffffffffffffe9ae2ed07577265dff7f94451e061e163c61L,
    h          = 0x04,
    size       = 238,
    bits       = 128,
    point_size = 36,
)

NAMED_CURVE['sect283r1'] = dict(
    f          = lambda x: x ** 283 + x ** 12 + x ** 7 + x ** 5 + 1,
    a          = 0x000000000000000000000000000000000000000000000000000000000000000000000001L,
    b          = 0x027b680ac8b8596da5a4af8a19a0303fca97fd7645309fa2a581485af6263e313b79a2f5L,
    G          = 0x0405f939258db7dd90e1934f8c70b0dfec2eed25b8557eac9c80e2e198f8cdbecd86b1205303676854fe24141cb98fe6d4b20d02b4516ff702350eddb0826779c813f0df45be8112f4L,
    n          = 0x03ffffffffffffffffffffffffffffffffffef90399660fc938a90165b042a7cefadb307L,
    h          = 0x02,
    size       = 283,
    bits       = 128,
    point_size = 36,
)

NAMED_CURVE['sect409k1'] = dict(
    f          = lambda x: x ** 409 + x ** 87 + 1,
    a          = 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000L,
    b          = 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001L,
    G          = 0x040060f05f658f49c1ad3ab1890f7184210efd0987e307c84c27accfb8f9f67cc2c460189eb5aaaa62ee222eb1b35540cfe902374601e369050b7c4e42acba1dacbf04299c3460782f918ea427e6325165e9ea10e3da5f6c42e9c55215aa9ca27a5863ec48d8e0286bL,
    n          = 0x7ffffffffffffffffffffffffffffffffffffffffffffffffffe5f83b2d4ea20400ec4557d5ed3e3e7ca5b4b5c83b8e01e5fcfL,
    h          = 0x04,
    size       = 409,
    bits       = 192,
    point_size = 52,
)

NAMED_CURVE['sect409r1'] = dict(
    f          = lambda x: x ** 409 + x ** 87 + 1,
    a          = 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001L,
    b          = 0x0021a5c2c8ee9feb5c4b9a753b7b476b7fd6422ef1f3dd674761fa99d6ac27c8a9a197b272822f6cd57a55aa4f50ae317b13545fL,
    G          = 0x04015d4860d088ddb3496b0c6064756260441cde4af1771d4db01ffe5b34e59703dc255a868a1180515603aeab60794e54bb7996a70061b1cfab6be5f32bbfa78324ed106a7636b9c5a7bd198d0158aa4f5488d08f38514f1fdf4b4f40d2181b3681c364ba0273c706L,
    n          = 0x010000000000000000000000000000000000000000000000000001e2aad6a612f33307be5fa47c3c9e052f838164cd37d9a21173L,
    h          = 0x02,
    size       = 409,
    bits       = 192,
    point_size = 52,
)

NAMED_CURVE['sect571k1'] = dict(
    f          = lambda x: x ** 571 + x ** 10 + x ** 5 + x ** 2 + 1,
    a          = 0x00,
    b          = 0x01,
    G          = 0x04026eb7a859923fbc82189631f8103fe4ac9ca2970012d5d46024804801841ca44370958493b205e647da304db4ceb08cbbd1ba39494776fb988b47174dca88c7e2945283a01c89720349dc807f4fbf374f4aeade3bca95314dd58cec9f307a54ffc61efc006d8a2c9d4979c0ac44aea74fbebbb9f772aedcb620b01a7ba7af1b320430c8591984f601cd4c143ef1c7a3L,
    n          = 0x020000000000000000000000000000000000000000000000000000000000000000000000131850e1f19a63e4b391a8db917f4138b630d84be5d639381e91deb45cfe778f637c1001L,
    h          = 0x04,
    size       = 571,
    bits       = 256,
    point_size = 72,
)

NAMED_CURVE['sect571r1'] = dict(
    f          = lambda x: x ** 571 + x ** 10 + x ** 5 + x ** 2 + 1,
    a          = 0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001L,
    b          = 0x02f40e7e2221f295de297117b7f3d62f5c6a97ffcb8ceff1cd6ba8ce4a9a18ad84ffabbd8efa59332be7ad6756a66e294afd185a78ff12aa520e4de739baca0c7ffeff7f2955727aL,
    G          = 0x040303001d34b856296c16c0d40d3cd7750a93d1d2955fa80aa5f40fc8db7b2abdbde53950f4c0d293cdd711a35b67fb1499ae60038614f1394abfa3b4c850d927e1e7769c8eec2d19037bf27342da639b6dccfffeb73d69d78c6c27a6009cbbca1980f8533921e8a684423e43bab08a576291af8f461bb2a8b3531d2f0485c19b16e2f1516e23dd3c1a4827af1b8ac15bL,
    n          = 0x03ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe661ce18ff55987308059b186823851ec7dd9ca1161de93d5174d66e8382e9bb2fe84e47L,
    h          = 0x02,
    size       = 571,
    bits       = 256,
    point_size = 72,
)

# Make sure all of our curves have a point_size
for name, params in NAMED_CURVE.iteritems():
    if not 'point_size' in params:
        try:
            params['point_size'] = num_bytes(params['p'])
        except KeyError:
            raise SyntaxError('Named curve {0} has no point_size or p'.format(
                name,
            ))
