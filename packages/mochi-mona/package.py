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
from spack import *


class MochiMona(CMakePackage):
    """A library that provides Argobots bindings to Mercury's underlying
    NA communication library for use in the context of Mochi projects."""

    homepage = 'https://xgitlab.cels.anl.gov/sds/mona'
    git = 'https://xgitlab.cels.anl.gov/sds/mona.git'

    version('master', branch='master', preferred=True)
    version('develop', branch='master')

    variant('benchmark', default=False,
            description='Build a benchmark to compare performance against MPI')

    depends_on('cmake@3.14:', type=('build'))
    depends_on('argobots@1.0:', type=("build", "link", "run"))
    depends_on('mercury@2.0.0', type=("build", "link", "run"))
    depends_on('mpi', when='+benchmark', type=("build", "link", "run"))

    # dependencies for develop version
    depends_on('mercury@master', type=("build", "link", "run"), when='@develop')

    def cmake_args(self):
        args = ['-DBUILD_SHARED_LIBS:BOOL=ON']
        if '+benchmark' in self.spec:
            args.append('-DENABLE_BENCHMARK:BOOL=ON')
            args.append('-DCMAKE_C_COMPILER=%s' % self.spec['mpi'].mpicc)
        return args
