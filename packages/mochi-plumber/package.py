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
from spack.package import *
from spack import *


class MochiPlumber(AutotoolsPackage):
    """a Mochi library for mapping processes to hardware resources."""

    homepage = "https://github.com/mochi-hpc/mochi-plumber"
    url      = "https://github.com/mochi-hpc/mochi-plumber/archive/v0.1.0.tar.gz"
    git      = 'https://github.com/mochi-hpc/mochi-plumber.git'

    version('develop', branch='main')
    version('main', branch='main')
    version('0.1.2', tag='v0.1.2')
    version('0.1.1', tag='v0.1.1')
    version('0.1.0', tag='v0.1.0')

    depends_on('m4', type='build')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('hwloc')
    depends_on('libfabric')

    # NOTE: The default autoreconf steps should work fine for this package.
    #       The explicit definition is just here as a workaround; Spack's
    #       default autoreconf step is prone to libtool version mismatch as
    #       of 2021/10/20.
    def autoreconf(self, spec, prefix):
        sh = which('sh')
        sh('./prepare.sh')
