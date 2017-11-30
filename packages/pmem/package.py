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
    url      = "https://github.com/pmem/nvml/archive/1.3.tar.gz"

    version('1.3',         'd1e843579a0b44301176bcd6142911cb')
    version('1.2.3',       '5e3fba2bf4fd6b0c16db4e91d32df4b0')
    version('1.2.2',       'f02832e9e0e2617e2c996f7b83b2e5ec')

    # experimental rpmem
    depends_on('libfabric@1.4.2:')
    # gcc7 warns about buffer overflows
    patch('0001-benchmark-fix-buffer-overflow-in-rpmem_persist.patch')

    def install(self, spec, prefix):
        make("install", "prefix=%s" % prefix)
