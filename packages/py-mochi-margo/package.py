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
#
# Installing py-margo:
#
#     spack install py-margo
#
from spack import *


class PyMochiMargo(PythonPackage):
    """Python wrapper for the Mochi Margo library"""

    homepage = 'https://github.com/mochi-hpc/py-mochi-margo'
    url      = 'https://github.com/mochi-hpc/py-mochi-margo/archive/refs/tags/v0.3.2.tar.gz'
    git      = 'https://github.com/mochi-hpc/py-mochi-margo.git'

    version('develop', branch='main')
    version('main', branch='main')
    version('0.4', sha256='8f2b8123299047f853883a98dc570582a5d22ed221f81899c75742e431e26f09')
    version('0.3.2', sha256='8aa04000b601fb4463e0b44a7ad562dba0b36f4105b83487d5f89341ee1faa82')
    version('0.3.1', sha256='f998aa7373e0b507685f9fe0dbb9d54f2bdf791d0e6d8fea112fdd7453edba29')
    version('0.3',   sha256='a574c91bf22dcd1bd54ea8bf87b00f257524e827b3afefc43bce01cf635acd73')
    version('0.2.4', sha256='b5a3605d977f566ced21229abe3c62e47833ea388c6ae031c973a4f332a1c77e')
    version('0.2.3', sha256='d0bc40b87c13d9351d616155db94c524476735a0557d1b2678a859bdfc93b727')
    version('0.2.2', sha256='539953d84842b4129d1c3fb8a09738dee6dfa6f5b2f48c6fdfe7567b26d27282')
    version('0.2.1', sha256='67851be5802005f1adb2b7122ed882b3e74293914e191001b3664bfe18dc84a5')
    version('0.2',   sha256='199e163bed9f6bf2fbed463dc6b4522630b80b4f9047ac28857dc29e695e8cae')
    version('0.1',   sha256='b32bb6e6b02185dc1180144987e28d4b1f2df4806c965c5d2290519d031cd202')

    depends_on('python')
    depends_on('py-numpy', when='@0.2:0.3.2')
    depends_on('py-setuptools', type=('build'))
    depends_on('py-pkgconfig', type=('build'))
    depends_on('py-pybind11', type=('build'))

    depends_on('mochi-margo@0.6:', when='@0.3:')
    depends_on('mochi-margo@0.4:')
    depends_on('mochi-margo@develop', when='@develop')
