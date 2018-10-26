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
import os


class Pmem(Package):
    """The NVM Library is a library for using memory-mapped persistence, optimized specifically for persistent memory"""

    homepage = "http://pmem.io/"
    url      = "https://github.com/pmem/nvml/archive/1.4.tar.gz"

    version('1.5',     sha256='6b069d7207febeb62440e89245e8b18fcdf40b6170d2ec2ef33c252ed16db2d4')
    # in the nvml -> pmdk name change, these hashes needed to be updated
    version('1.4.2',     sha256='df7e658e75d28cd80f6d2ff7b9fc9ae2885d52f8923fdbacecfd46215115fb4c')
    version('1.4',       '8813455d9518b8d7e0c296a706314940')
    version('1.3',         '32c41d0d7f1c855b7d2b9622631a6bc3')

    # experimental rpmem
    #depends_on('libfabric@1.4.2:')

    # documentation requires doxygen and a bunch of other depenedncies that
    # were not working properly on our contianers
    patch('0001-make-doc-building-explicit.patch')
    patch('0002-remove-secure-getenv.patch', when='@1.4:')

    def install(self, spec, prefix):
        make("install", "prefix=%s" % prefix, "NDCTL_ENABLE=n", "EXTRA_CFLAGS=-Wno-error", "BUILD_RPMEM=n")
