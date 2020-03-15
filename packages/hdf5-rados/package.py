# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Hdf5Rados(CMakePackage):
    """The HDF5 RADOS VOL connector is an external VOL connector that interfaces with the RADOS API"""

    homepage = ''
    url = ''
    git = 'https://git.hdfgroup.org/scm/hdf5vol/rados-api.git'

    maintainers = ['soumagne']

    version('master', branch='master', submodules=True)

    variant('mobject', default=True, description='Use mobject')

    depends_on('cmake@2.8.12.2:', type='build')
    depends_on('mobject', when='+mobject')
    depends_on('hdf5@1.12.0:+mpi')

    def cmake_args(self):
        """Populate cmake arguments for HDF5 RADOS."""
        spec = self.spec
        variant_bool = lambda feature: str(feature in spec)
        parallel_tests = '+mpi' in spec and self.run_tests

        cmake_args = [
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DBUILD_TESTING:BOOL=%s' % str(self.run_tests),
            '-DHDF5_VOL_RADOS_USE_MOBJECT:BOOL=%s'
            % variant_bool('+mobject'),
        ]

        return cmake_args

    def check(self):
        """Unit tests fail when run in parallel."""

        with working_dir(self.build_directory):
            make('test', parallel=False)
