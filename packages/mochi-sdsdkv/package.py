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


class MochiSdsdkv(AutotoolsPackage):
    """a Mochi library that provides a distributed Margo-based keyval service"""

    homepage = 'https://github.com/mochi-hpc/mochi-sdsdkv'
    url = 'https://github.com/mochi-hpc/mochi-sdsdkv'
    git = 'https://github.com/mochi-hpc/mochi-sdsdkv.git'

    version('main', branch='main')
    version('develop', branch='main')
    version('0.1', tag='v0.1')

    depends_on('autoconf@2.65:')
    depends_on('automake@1.13.4:')
    depends_on('libtool', type=("build"))

    depends_on('mochi-sdskv +leveldb~bwtree~bdb')
    depends_on('mochi-ssg+mpi@0.2', when='@0.1')
    depends_on('mochi-ch-placement')

    # dependencies for develop version
    depends_on('mochi-sdskv +leveldb~bwtree~bdb @develop', when='@develop')
    depends_on('mochi-ssg+mpi@develop', when='@develop')
    depends_on('mochi-ch-placement@develop', when='@develop')

    patch('0001-update-missing-configure-macros.patch', when='@0.1')

    def autoreconf(self, spec, prefix):
        autogen = Executable('./autogen')
        autogen()

    def configure_args(self):
        return [
            'CXX={0}'.format(self.spec['mpi'].mpicxx)
        ]
