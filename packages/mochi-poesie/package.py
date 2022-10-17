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


class MochiPoesie(CMakePackage):
    """A Mochi library that provides a Margo-based embedded scripting service"""

    homepage = 'https://github.com/mochi-hpc/mochi-poesie'
    url = 'https://github.com/mochi-hpc/mochi-poesie/archive/refs/tags/v0.2.tar.gz'
    git = 'https://github.com/mochi-hpc/mochi-poesie.git'

    version('develop', branch='main')
    version('main', branch='main')
    version("0.2", sha256="dafbdcdd8feb8d81f0dd31cc329c3656e22c8381b5c6a628e57567822190e9d3")

    variant('lua',    default=True, description="Enable Lua interpreters")
    variant('python', default=True, description="Enable Python interpreters")
    variant('bedrock', default=False, description="Enable Bedrock support")

    depends_on('mochi-margo@0.9:')
    depends_on('mochi-margo@develop', when='@develop')
    depends_on('mochi-bedrock', when='+bedrock')
    depends_on('mochi-bedrock@develop', when='+bedrock @develop')

    depends_on('json-c')
    depends_on('lua', when="+lua")
    depends_on('python@3.6:', when="+python")

    def cmake_args(self):
        args = []
        variant_bool = lambda feature: str(feature in self.spec)
        args.append('-DENABLE_PYTHON:BOOL=%s' % variant_bool('+python'))
        args.append('-DENABLE_LUA:BOOL=%s' % variant_bool('+lua'))
        args.append('-DENABLE_BEDROCK:BOOL=%s' % variant_bool('+bedrock'))
        return args
