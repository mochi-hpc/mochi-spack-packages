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


class PyMochiBedrock(PythonPackage):
    """Mochi Bedrock's Python library and wrapper."""

    homepage = 'https://github.com/mochi-hpc/py-mochi-bedrock'
    url      = 'https://github.com/mochi-hpc/py-mochi-bedrock/archive/refs/tags/v0.1.tar.gz'
    git      = 'https://github.com/mochi-hpc/py-mochi-bedrock.git'

    version('develop', branch='main')
    version('main', branch='main')
    version('0.2', sha256='833c871f9811d0a498512fe96784e6a55fa923b3ffbdafc708a32dbf47c67733')
    version('0.1', sha256='dd479475c90b357d0f9d6c5b0c8425609fa0170bc5316efafe1adb53e9c21ab5')

    variant('client', default=False, when='@0.2:',
            description="Build the C++ extension for the Bedrock client")

    depends_on('python@3.6:')
    depends_on('py-attrs@20.3.0:')
    depends_on('py-setuptools', type=('build'))
    depends_on('py-pkgconfig', type=('build'), when='+client')
    depends_on('py-pybind11', type=('build'), when='+client')
    depends_on('mochi-bedrock@0.3:', when='+client')

    def setup_build_environment(self, env):
        if '+client' in self.spec:
            env.set('BUILD_PY_BEDROCK_CLIENT', '1')
