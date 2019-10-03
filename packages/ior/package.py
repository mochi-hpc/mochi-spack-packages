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


    version('develop', branch='master', submodules=True)
    version('hdf5-rados', branch='hdf5-rados-ior', submodules=True)
    version('3.2.0',    sha256='0cda0e00b7f070c6754ef8acb3873eb3a625bd8dee3f2e220291656be1322bbb')
    version('3.0.1', '71150025e0bb6ea1761150f48b553065')

    variant('hdf5',  default=False, description='support IO with HDF5 backend')
    variant('ncmpi', default=False, description='support IO with NCMPI backend')
    variant('rados', default=False, description='support IO with RADOS backend')
    variant('mobject', default=False, description='support IO with RADOS-like Mobject backend')
    variant('gpfs', default=False, description='support configurable GPFS in IOR')

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
            #env['CC'] = 'h5pcc'
        else:
            config_args.append('--without-hdf5')

        if '+ncmpi' in spec:
            config_args.append('--with-ncmpi')
        else:
            config_args.append('--without-ncmpi')

        if '+rados' in spec:
            config_args.append('--with-rados')
        else:
            config_args.append('--without-rados')

        if '+mobject' in spec:
            pkg_config=which('pkg-config')
            extra_libs="LIBS="
            extra_libs += subprocess.check_output([str(pkg_config), "--libs-only-l", "mobject-store"]).strip('\n')
            config_args.append('--with-rados')
            config_args.append(extra_libs)
        else:
            config_args.append('--without-rados')

        if '-gpfs' in self.spec:
            config_args.append('--without-gpfs')

        return config_args
