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
# Installing py-remi:
#
#     spack install py-remi
#
from spack import *

class PyMochiRemi(PythonPackage):
    """Python wrapper for the Mochi REMI library"""

    homepage = 'https://github.com/mochi-hpc/py-mochi-remi'
    url      = 'https://github.com/mochi-hpc/py-mochi-remi'
    git      = 'https://github.com/mochi-hpc/py-mochi-remi.git'

    version('develop',  branch='main')
    version('main',  branch='main')
    version('0.1.2', tag='v0.1.2')
    version('0.1.1', tag='v0.1.1')
    version('0.1', tag='v0.1')

    depends_on('py-pkgconfig', type=('build'))
    depends_on('py-pybind11', type=('build'))
    depends_on('py-setuptools', type=('build'))
    depends_on('mochi-remi@0.1:')
    depends_on('py-mochi-margo@0.1:')

    depends_on('mochi-remi@develop', when='@develop')
    depends_on('py-mochi-margo@develop', when='@develop')
