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
from spack import *


class MochiChPlacement(AutotoolsPackage):
    """a Mochi library for consistent hashing with modular algorithms.
    It can be used by a distributed storage system to access multiple
    hashing algorithms, distance metrics, and virtual node settings using a consistent API."""

    homepage = "https://github.com/mochi-hpc/mochi-ch-placement"
    url      = "https://github.com/mochi-hpc/mochi-ch-placement/archive/v0.1.tar.gz"
    git      = 'https://github.com/mochi-hpc/mochi-ch-placement.git'

    version('develop', branch='main')
    version('0.1', tag='v0.1')

    depends_on('m4')
    depends_on('autoconf')
    depends_on('automake')
    depends_on('libtool')

    # NOTE: The default autoreconf steps should work fine for this package.
    #       The explicit definition is just here as a workaround; Spack's
    #       default autoreconf step is prone to libtool version mismatch as
    #       of 2021/10/20.
    def autoreconf(self, spec, prefix):
        sh = which('sh')
        sh('./prepare')
