# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class MochiYcsbBackends(CMakePackage):
    """Mochi-based DB backends for the YCSB benchmark."""

    homepage = "https://github.com/mochi-hpc/mochi-ycsb-backends"
    url = "https://github.com/mochi-hpc/mochi-ycsb-backends/archive/refs/tags/v0.1.tar.gz"
    git = "https://github.com/mochi-hpc/mochi-ycsb-backends.git"

    version('develop', branch='main')
    version('main', branch='main')

    depends_on('cmake@3.15:', type='build')
    depends_on('openjdk', type='build')
    depends_on('ycsb@0.17.0')

    def cmake_args(self):
        args = []
        args.append('-DYCSB_ROOT=%s' % self.spec['ycsb'].prefix)
        return args
