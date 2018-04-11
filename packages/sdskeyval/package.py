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


class Sdskeyval(AutotoolsPackage):
    """a library that provides a Margo-based keyval service"""

    homepage = "https://xgitlab.cels.anl.gov/sds/sds-keyval"
    url = "https://xgitlab.cels.anl.gov/sds/sds-keyval"

    version('master', git='https://xgitlab.cels.anl.gov/sds/sds-keyval.git')
    version('dor-sds', git='https://xgitlab.cels.anl.gov/sds/sds-keyval.git', branch='dor-sync-review')

    variant('bwtree', default=True, description="Enable BwTree keyval backend")
    variant('bdb', default=True, description="Enable Berkely DB keyval backend")
    variant('leveldb', default=True, description="Enable LevelDB keyval backend")
    variant('lmdb', default=False, description="Enable lmdb keyval backend")

    depends_on('margo', type=("build", "link", "run"))
    depends_on('autoconf@2.65:')
    depends_on('automake@1.13.4:')
    depends_on('libtool', type=("build"))
    depends_on('ch-placement')
    depends_on('ssg+mpi')
    depends_on('boost+system+filesystem')

    # variable dependencies
    depends_on('berkeley-db', when="+bdb")
    depends_on('leveldb', when="+leveldb")

    # requires c++11 if bwtree selected
    conflicts('%gcc@:4.8.0', when="+bwtree")
    # clang fullly implemented C++11 in 3
    # intel implemented c++11 in 13.0
    # but neither clang nor intel compile the BwTree data structure
    conflicts('%clang', when="+bwtree")
    conflicts('%intel', when="+bwtree")

    def configure_args(self):
        spec = self.spec
        extra_args = []

	extra_args.extend([
		"--with-boost-libdir="
		+ spec['boost'].prefix +'/lib'])
        extra_args.extend([
            "CXXFLAGS=-std=c++11"
            ])
        if '+bdb' in spec:
            extra_args.extend([
                "--with-berkeleydb="
		+ spec['berkeley-db'].prefix
                ])
        if '+leveldb' in spec:
            extra_args.extend([
                "--enable-leveldb"
                ])

        # cray compilers needed -latomic to build BwTree;
        # gcc7, at least on my Ubuntu laptop did, also
        if '+bwtree' in spec:
            if 'platform=cray' in self.spec:
                extra_args.extend(['LDFLAGS=-latomic'])
            if spec.compiler.name == "gcc" and spec.compiler.version >= Version('7'):
                extra_args.extend(['LDFLAGS=-latomic'])

        return extra_args

