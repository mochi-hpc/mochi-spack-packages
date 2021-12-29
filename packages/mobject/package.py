##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
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


class Mobject(AutotoolsPackage):
    """A Mochi microservice object store built on Margo, sds-keyval, and other components"""

    homepage = 'https://github.com/mochi-hpc/mobject'
    url = 'https://github.com/mochi-hpc/mobject/archive/refs/tags/v0.5.tar.gz'
    git = 'https://github.com/mochi-hpc/mobject.git'

    # Note: version 0.5 has become unsatisfiable because mobject requires mochi-ssg@0.4.5
    # but also mochi-bedrock, which requires at least mochi-ssg@0.4.6.

    version('main', branch='main')
    version('develop', branch='main')
    version('0.6', sha256='6c58df9a58d8bd9394fb4fc5538fcc39cbddee344864af5038ca60cdb2ac08fe')
    #version('0.5', sha256='ac612e6fe3b85ee54b00c7e08e51689a0eda7ffa057085a5df5053476ada86bc')
    version('0.4.3', tag='v0.4.3')
    version('0.4.2', tag='v0.4.2')
    version('0.4.1', tag='v0.4.1')
    version('0.4', tag='v0.4')
    version('0.3', tag='v0.3')
    version('0.2', tag='v0.2')
    version('0.1', tag='v0.1')

    variant('timing', default=False, description="crude timing information")

    depends_on('mpi', when='@:0.4.1')
    depends_on('autoconf')
    depends_on('automake')
    depends_on('libtool')

    # Mochi dependencies for normal versions
    depends_on('mochi-margo @0.4:')
    depends_on('mochi-margo @0.9.4:', when='@0.5:')
    depends_on('mochi-ssg +mpi @0.2', when='@:0.3')
    depends_on('mochi-ssg +mpi @0.4.0:', when='@0.4:0.4.1')
    #depends_on('mochi-ssg @0.4.5', when='@0.5')
    depends_on('mochi-ssg @0.5:', when='@0.6:')
    depends_on('mochi-ch-placement @0.1:')
    depends_on('mochi-sdskv @0.1:')
    depends_on('mochi-sdskv +bedrock @0.1.13:', when='@0.5:')
    depends_on('mochi-bake @0.1:')
    depends_on('mochi-bake @0.3:0.3.6', when='@:0.4.1')
    depends_on('mochi-bake @0.4:', when='@0.4.2')
    depends_on('mochi-bake @0.6:', when='@0.4.3:')
    depends_on('mochi-bake +bedrock @0.6.3:', when='@0.5:')
    depends_on('mochi-bedrock @0.3:', when='@0.5:')

    # Mochi dependencies for develop version
    depends_on('mochi-margo @develop', when='@develop')
    depends_on('mochi-ssg+mpi @develop', when='@develop')
    depends_on('mochi-ch-placement @develop', when='@develop')
    depends_on('mochi-sdskv +bedrock @develop', when='@develop')
    depends_on('mochi-bake +bedrock @develop', when='@develop')

    patch('0001-crude-timing-information.patch', when='+timing @:0.4.1')

    # NOTE: The default autoreconf steps should work fine for this package.
    #       The explicit definition is just here as a workaround; Spack's
    #       default autoreconf step is prone to libtool version mismatch as
    #       of 2021/10/20.
    def autoreconf(self, spec, prefix):
        sh = which('sh')
        sh('./prepare.sh')

    def configure_args(self):
        extra_args = []
        if self.version < Version('0.5'):
            extra_args.extend(['CC=%s' % self.spec['mpi'].mpicc])
            extra_args.extend(['CXX=%s' % self.spec['mpi'].mpicxx])
        return extra_args
