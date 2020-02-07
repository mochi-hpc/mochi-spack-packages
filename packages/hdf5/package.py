# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import shutil
import sys
import subprocess

from spack.pkg.builtin.hdf5 import Hdf5

class Hdf5(Hdf5):

    version('extvol-develop', commit='474b0571462956d282331a9ee12c208d50f41032')
    version('rados-develop', branch='feature/rados_vol')
    version('rados-old', branch='feature/hdf5_rados')

    variant('mobject', default=False, description='Enable support for MObject')
    depends_on('mobject@develop', when='+mobject')

    def configure_args(self):
        config_args = super().configure_args()

        if '+mobject' in self.spec:
            pkg_config = which('pkg-config')
            extra_libs = "LIBS=%s" % pkg_config('--libs-only-l', "mobject-store",
                                                output=str).strip('\n')
            config_args.append(extra_libs)

            extra_cflags = "CPPFLAGS=-DHDF5_USE_MOBJECT %s" % pkg_config('--cflags',
                                          'mobject-store', output=str).strip('\n')
            config_args.append(extra_cflags)

            config_args.append('--with-rados')

        return config_args
