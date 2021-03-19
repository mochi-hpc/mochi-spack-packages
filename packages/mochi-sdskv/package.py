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


class MochiSdskv(AutotoolsPackage):
    """A Mochi library that provides a Margo-based keyval service"""

    homepage = "https://github.com/mochi-hpc/mochi-sdskv"
    url = "https://github.com/mochi-hpc/mochi-sdskv"
    git = "https://github.com/mochi-hpc/mochi-sdskv.git"

    version('dev-bedrock', branch='dev-bedrock');
    version('develop', branch='main')
    version('main', branch='main')
    version('0.1.10', tag='v0.1.10')
    version('0.1.9', tag='v0.1.9')
    version('0.1.8', tag='v0.1.8')
    version('0.1.7.1', tag='v0.1.7.1')
    version('0.1.7', tag='v0.1.7')
    version('0.1.6', tag='v0.1.6')
    version('0.1.5', tag='v0.1.5')
    version('0.1.4', tag='v0.1.4')
    version('0.1.3', tag='v0.1.3')
    version('0.1.2', tag='v0.1.2')
    version('0.1.1', tag='v0.1.1')
    version('0.1', tag='v0.1')

    variant('benchmark', default=False, description='Compiles a benchmark')
    variant('remi', default=False, description="Enables migration support using REMI")
    variant('bdb', default=True, description="Enable Berkely DB keyval backend")
    variant('leveldb', default=True, description="Enable LevelDB keyval backend")
    variant('lmdb', default=False, description="Enable lmdb keyval backend")
    variant('bedrock', default=True, description="Enable bedrock (Mochi loader")

    depends_on('autoconf@2.65:')
    depends_on('automake@1.13.4:')
    depends_on('libtool', type=("build"))
    depends_on('jsoncpp@1.9.1:', when='+benchmark')
    depends_on('mpi', when='+benchmark')
    depends_on('mochi-margo@0.4:', type=("build", "link", "run"), when='@:0.1.3')
    depends_on('mochi-margo@0.5.2:', type=("build", "link", "run"), when='@0.1.4:')
    depends_on('mochi-abt-io', type=("build", "link", "run"))
    depends_on('mochi-remi@0.1:', when='@:0.1.1')
    depends_on('mochi-remi@0.2.1:', when='@0.1.2:0.1.3')
    depends_on('mochi-remi@0.2.2:', when='+remi @0.1.4:')

    # dependencies for develop version
    depends_on('mochi-margo@develop', when='@develop')
    depends_on('mochi-abt-io@develop', when='@develop')
    depends_on('mochi-remi@develop', when='+remi @develop')

    # variable dependencies
    depends_on('berkeley-db', when="+bdb")
    depends_on('leveldb', when="+leveldb")
    depends_on('mochi-bedrock', when="+bedrock")

    def configure_args(self):
        spec = self.spec
        extra_args = []

        if '+bdb' in spec:
            extra_args.extend([
                "--with-berkeleydb="
            + spec['berkeley-db'].prefix
                ])
        if '+leveldb' in spec:
            extra_args.extend([
                "--enable-leveldb"
                ])

        if '+benchmark' in spec:
            extra_args.append('--enable-benchmark')
            extra_args.append('CXX=%s' % spec['mpi'].mpicxx)
        else:
            extra_args.append('--disable-benchmark')

        if spec.satisfies('@0.1.4:'):
            if '+remi' in spec:
                extra_args.append('--enable-remi')
            else:
                extra_args.append('--disable-remi')
        if '+bedrock' in spec:
            extra_args.append('--enable-bedrock')
        else:
            extra_args.append('--disable-bedrock')

        return extra_args
