# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *
from spack.package import *


class YcsbCppInterface(CMakePackage):
    """Java/C++ library to enable writing YCSB DB implementations in C++."""

    homepage = "https://github.com/mochi-hpc/ycsb-cpp-interface"
    url = "https://github.com/mochi-hpc/ycsb-cpp-interface/archive/refs/tags/v0.1.tar.gz"
    git = "https://github.com/mochi-hpc/ycsb-cpp-interface.git"

    version('develop', branch='main')
    version('main', branch='main')

    depends_on('cmake@3.15:', type='build')
    depends_on('openjdk', type='build')
    depends_on('ycsb@0.17.0:')

    def cmake_args(self):
        args = []
        args.append('-DYCSB_ROOT=%s' % self.spec['ycsb'].prefix)
        return args
