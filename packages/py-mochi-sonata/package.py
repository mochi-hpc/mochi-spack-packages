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


class PyMochiSonata(PythonPackage):
    """Python wrapper for the Mochi Sonata library"""

    homepage = 'https://github.com/mochi-hpc/py-mochi-sonata'
    url      = 'https://github.com/mochi-hpc/py-mochi-sonata/archive/refs/tags/v0.1.2.tar.gz'
    git      = 'https://github.com/mochi-hpc/py-mochi-sonata.git'

    version('develop', branch='main')
    version('main', branch='main')
    version('0.1.2', sha256='e72a6e9dde563fa2f6fba9a9808e91dd035aa02d16d82e20a794a7b916da1e55')
    version('0.1.1', sha256='95cdb62edd7661917bbc0baaa5a4f3e50eb2d174c2571ed6c43c4c50873d48c8')
    version('0.1',   sha256='d91a9ba7786d87e5fe5576ac72fcae9a5393fa8088cfd047dc8b31a5252bda83')

    depends_on('python')
    depends_on('py-pkgconfig', type=('build'))
    depends_on('py-pybind11', type=('build'))
    depends_on('py-mochi-margo')
    depends_on('mochi-sonata@0.5:')
