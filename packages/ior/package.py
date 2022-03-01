# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.ior import Ior as BuiltinIor

class Ior(BuiltinIor):

    git = 'https://github.com/shanedsnyder/ior'
    version('develop', branch='master', submodules=True)
    version('master', branch='master', submodules=True)
    version('hdf5-rados', branch='hdf5-rados-ior', submodules=True)

    variant('rados', default=False, description='support IO with RADOS backend')
    variant('mobject', default=False, description='support IO with RADOS-like Mobject backend')
    variant('gpfs', default=False, description='support configurable GPFS in IOR')

    # depend on latest mobject to bring in latest bake
    depends_on('mobject@0.4.2:', when='+mobject')
    depends_on('mobject@develop', when='+mobject @develop')
    # rados and mobject are incompatible
    conflicts('+mobject', when='+rados')
    conflicts('+rados', when='+mobject')

    patch('0001-DO-NOT-MERGE-mobject-specific-hackery.patch', when='+mobject')

    def configure_args(self):
        spec = self.spec
        config_args = super(Ior, self).configure_args()

        if '+rados' in spec:
            config_args.append('--with-rados')

        if '+mobject' in spec:
            extra_libs = "LIBS="
            pkg_config = which('pkg-config')
            extra_libs += pkg_config('--libs-only-l', "mobject-store",
                                     output=str)

            config_args.append('--with-rados')
            config_args.append(extra_libs)

        return config_args
