# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import subprocess
import os


class Ior(AutotoolsPackage):
    """The IOR software is used for benchmarking parallel file systems
    using POSIX, MPI-IO, or HDF5 interfaces."""

    homepage = "https://github.com/hpc/ior"
    url      = "https://github.com/hpc/ior/archive/3.2.0.tar.gz"
    git = 'https://github.com/shanedsnyder/ior'


    version('mobject', branch='mobject-ior', submodules=True)
    version('3.2.0',    sha256='0cda0e00b7f070c6754ef8acb3873eb3a625bd8dee3f2e220291656be1322bbb')
    version('3.0.1', '71150025e0bb6ea1761150f48b553065')

    variant('hdf5',  default=False, description='support IO with HDF5 backend')
    variant('ncmpi', default=False, description='support IO with NCMPI backend')
    variant('mobject', default=False, description='support IO with RADOS-like Mobject backend')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')
    depends_on('mpi')
    depends_on('hdf5+mpi', when='+hdf5')
    depends_on('parallel-netcdf', when='+ncmpi')
    depends_on('mobject', when='+mobject')

    patch('0001-DO-NOT-MERGE-mobject-specific-hackery.patch', when='+mobject')

    @run_before('autoreconf')
    def bootstrap(self):
        Executable('./bootstrap')()

    def configure_args(self):
        spec = self.spec
        config_args = []

        env['CC'] = spec['mpi'].mpicc

        if '+hdf5' in spec:
            config_args.append('--with-hdf5')
            config_args.append('CFLAGS=-D H5_USE_16_API')
        else:
            config_args.append('--without-hdf5')

        if '+ncmpi' in spec:
            config_args.append('--with-ncmpi')
        else:
            config_args.append('--without-ncmpi')

	if '+mobject' in spec:
	    os.environ["PKG_CONFIG_ALLOW_SYSTEM_CFLAGS"]="yes"
	    pkg_config=which('pkg-config')
	    extra_cflags = "CPPFLAGS="
	    extra_ldflags="LDFLAGS="
	    extra_cflags  += subprocess.check_output([str(pkg_config), "--cflags",  "mobject-store"]).strip('\n')
	    extra_ldflags += subprocess.check_output([str(pkg_config), "--libs", "mobject-store"]).strip('\n')
	    config_args.append('--with-rados')
	    config_args.append(extra_cflags)
	    config_args.append(extra_ldflags)

        return config_args
