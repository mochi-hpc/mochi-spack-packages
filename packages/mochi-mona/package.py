##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack.package import *
from spack import *


class MochiMona(CMakePackage):
    """A library that provides Argobots bindings to Mercury's underlying
    NA communication library for use in the context of Mochi projects."""

    homepage = 'https://github.com/mochi-hpc/mochi-mona'
    url = 'https://github.com/mochi-hpc/mochi-mona/archive/refs/tags/v0.1.tar.gz'
    git = 'https://github.com/mochi-hpc/mochi-mona.git'

    version("0.3.0", sha256="f783636fbc77a2289c13d348f43a0b9f5d1c2e7c258aa7228c59d6e7023f56f6")
    version('0.2.3', sha256='cf9822d12c901b80a3fe029bf128d2b03ce897aabea4a0ea827eeb761bdcb405')
    version('0.2.2', sha256='c6ac88c98e622dfa87743a4b5649eaa247fb886a707442f8bc5ff918c5ede93d')
    version('0.2.1', sha256='deae5677d99410c908f7844f46ec83b3ade4498750e25836446f4a6346470b92')
    version('0.2', sha256='e14dab43a42afb6fcc0f362f4feeec9599381e101d4c594a6feb3db71dc5e000')
    version('0.1.1', sha256='574d29a4751b27c9ba8a2b17c8d157186604137f6025ec3e8402f14eed18e5bd')
    version('0.1', sha256='815be710beafebb0cf4b1b78ba83781982849ef962dfa66e46adae027dff88e8')
    version('main', branch='main')
    version('develop', branch='main')

    variant('benchmark', default=False,
            description='Build a benchmark to compare performance against MPI')
    variant('mpi', default=False, when='@0.2:',
            description='Build and install library of MPI wrappers')

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on('cmake@3.14:', type=('build'))
    depends_on('argobots@1.0:', type=("build", "link", "run"))
    depends_on('mercury@2.0.0:2.2.0', type=("build", "link", "run"), when='@0.1:0.2.3')
    depends_on('mercury@2.3.0:', type=("build", "link", "run"), when='@main,0.3.0:')
    depends_on('mpi', when='+benchmark', type=("build", "link", "run"))
    depends_on('mpi', when='+mpi', type=("build", "link", "run"))

    # dependencies for develop version
    depends_on('mercury@master', type=("build", "link", "run"), when='@develop')

    # note: a change in mercury > 2.2.0 (na_addr_t no longer a pointer)
    # will require mona to be updated once a new release of mercury lands.

    def cmake_args(self):
        args = ['-DBUILD_SHARED_LIBS:BOOL=ON']
        if '+benchmark' in self.spec:
            args.append('-DENABLE_BENCHMARK:BOOL=ON')
        if '+mpi' in self.spec:
            args.append('-DENABLE_MPI_WRAPPERS:BOOL=ON')
        if '+benchmark' in self.spec or '+mpi' in self.spec:
            args.append('-DCMAKE_C_COMPILER=%s' % self.spec['mpi'].mpicc)
            args.append('-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx)
        return args
