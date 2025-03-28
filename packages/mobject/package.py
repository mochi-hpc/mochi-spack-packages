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
from spack.package import *
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
    version('0.7rc1', tag='v0.7rc1')
    version("0.6.1", sha256="ce2ee0249acee7d2d0e1b62782fe67000d42566c8cbe27be116c1e35f8fad049")
    version('0.6', sha256='6c58df9a58d8bd9394fb4fc5538fcc39cbddee344864af5038ca60cdb2ac08fe')
    version('0.4.3', tag='v0.4.3')
    version('0.4.2', tag='v0.4.2')
    version('0.4.1', tag='v0.4.1')
    version('0.4', tag='v0.4')
    version('0.3', tag='v0.3')
    version('0.2', tag='v0.2')
    version('0.1', tag='v0.1')

    variant('timing', default=False, description="crude timing information")
    variant('bedrock', default=True, description='Enable Bedrock support')

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on('mpi', when='@:0.4.1')
    depends_on('autoconf')
    depends_on('automake')
    depends_on('libtool')

    # NOTE: uses yokan up to 0.3.0 because of the API break in
    # next versions. Need to change mobject in the future
    # to adapt to the new Yokan API.

    # Mochi dependencies for normal versions
    depends_on('mochi-margo @0.4:')
    depends_on('mochi-margo @0.9.4:', when='@0.5:')
    depends_on('mochi-ssg +mpi @0.2', when='@:0.3')
    depends_on('mochi-ssg +mpi @0.4.0:', when='@0.4:0.4.1')
    depends_on('mochi-ssg @0.5:', when='@0.6:')
    depends_on('mochi-ch-placement @0.1:')
    depends_on('mochi-sdskv @0.1:', when='@:0.6.1')
    depends_on('mochi-sdskv @0.1.13:', when='@0.5:0.6.1')
    depends_on('mochi-sdskv +bedrock @0.1.13:', when='@0.5:0.6.1 +bedrock')
    depends_on('mochi-yokan @0.2.10:0.3.0', when='@0.7:')
    depends_on('mochi-yokan +bedrock @0.2.10:0.3.0', when='@0.7rc1,0.7: +bedrock')
    depends_on('mochi-bake @0.1:')
    depends_on('mochi-bake @0.3:0.3.6', when='@:0.4.1')
    depends_on('mochi-bake @0.4:', when='@0.4.2')
    depends_on('mochi-bake @0.6:', when='@0.4.3:')
    depends_on('mochi-bake @0.6.3:', when='@0.5:')
    depends_on('mochi-bake +bedrock @0.6.3:', when='@0.5: +bedrock')
    depends_on('mochi-bedrock @0.3:0.14.2', when='@0.5: +bedrock')

    # Mochi dependencies for develop version
    depends_on('mochi-margo @develop', when='@develop')
    depends_on('mochi-ssg+mpi @develop', when='@develop')
    depends_on('mochi-ch-placement @develop', when='@develop')
    depends_on('mochi-yokan @:0.3.0', when='@develop')
    depends_on('mochi-yokan +bedrock @:0.3.0', when='@develop +bedrock')
    depends_on('mochi-bake @develop', when='@develop')
    depends_on('mochi-bake +bedrock @develop', when='@develop +bedrock')

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
        if '+bedrock' in self.spec:
            extra_args.append('--enable-bedrock')
        else:
            extra_args.append('--disable-bedrock')

        if self.version < Version('0.5'):
            extra_args.extend(['CC=%s' % self.spec['mpi'].mpicc])
            extra_args.extend(['CXX=%s' % self.spec['mpi'].mpicxx])
        return extra_args
