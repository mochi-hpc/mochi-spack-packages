# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
try:
    from spack_repo.builtin.packages.mercury.package import Mercury as BuiltinMercury
except ImportError:
    from spack.pkg.builtin.mercury import Mercury as BuiltinMercury


class Mercury(BuiltinMercury):

    git = 'https://github.com/mercury-hpc/mercury.git'

    # note that these may be duplicated upstream; we repeat them here to
    # make sure that newer versions of Mercury are available for people on
    # older spack releases

    version("2.4.2-mdorier-new-na", branch="mdorier/new-na-backends",
            git="https://github.com/mdorier/mercury.git",
            submodules=True)
    version("2.4.1", sha256="8a372416f3fca28d402ac7f7b73f0a7dd5d4b88785281ad9e6076e105e4840b9")
    version("2.4.0", sha256="8926cd177f6e3c04e8ae1683d42f7c8b27163a93d4d99a305fe497fa8ca86e79")
    version("2.3.1", sha256="36182d49f2db7e2b075240cab4aaa1d4ec87a7756450c87643ededd1e6f16104")
    version("2.3.0", sha256="e9e62ce1bb2fd482f0e85ad75fa255d9750c6fed50ba441a03de93b3b8eae742")
    version("2.2.0", sha256="e66490cf63907c3959bbb2932b5aaf51d96a481b17f0935f409f3a862eff97f6")
    version('2.1.0', sha256='9a58437161e9273b1b1c484d2f1a477a89eea9afe84575415025d47656f3761b')
    version('2.0.1', sha256='335946d9620ac669643ffd9861a5fb3ee486834bab674b7779eaac9d6662e3fa')
    version('2.0.0', sha256='9e80923712e25df56014309df70660e828dbeabbe5fcc82ee024bcc86e7eb6b7')

    variant('ucx', default=False, description='Use UCX plugin')
    variant("psm", default=False, when="@2.2.0:", description="Use PSM plugin")
    variant("psm2", default=False, when="@2.2.0:", description="Use PSM2 plugin")
    variant(
        "hwloc", default=False, when="@2.2.0:", description="Use hwloc to retrieve NIC information"
    )

    variant("quic", when="@2.4.2-mdorier-new-na", default=False, description="Use QUIC plugin")
    variant("zmq", when="@2.4.2-mdorier-new-na", default=False, description="Use ZMQ plugin")
    variant("http", when="@2.4.2-mdorier-new-na", default=False, description="Use HTTP plugin")

    depends_on('ucx', when='+ucx')
    depends_on('opa-psm2', when='+psm2')
    depends_on('opa-psm2', when='+psm')

    depends_on('lsquic+shared', when='+quic')
    depends_on('libzmq', when='+zmq')
    depends_on('curl', when='+http')
    depends_on('libmicrohttpd', when='+http')

    # note that the usptream mercury package is more selective about when
    # which combinations are valid; in the mochi-spack-packages repo we take
    # a simpler approach since this is an inherited package.
    def cmake_args(self):
        args = super(Mercury, self).cmake_args()
        spec = self.spec
        variant_bool = lambda feature: str(feature in spec)
        args.append('-DNA_USE_UCX:BOOL=%s' % variant_bool('+ucx'))
        args.append('-DNA_USE_PSM:BOOL=%s' % variant_bool('+psm'))
        args.append('-DNA_USE_PSM2:BOOL=%s' % variant_bool('+psm2'))
        args.append('-DNA_USE_LSQUIC:BOOL=%s' % variant_bool('+quic'))
        args.append('-DNA_USE_ZMQ:BOOL=%s' % variant_bool('+zmq'))
        args.append('-DNA_USE_HTTP:BOOL=%s' % variant_bool('+http'))
        args.append('-DNA_OFI_USE_HWLOC:BOOL=%s' % variant_bool('hwloc'))
        return args
