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
# Installing py-bake:
#
#     spack install py-bake
#
from spack import *

class PyMochiBake(PythonPackage):
    """Python wrapper for the Mochi Bake library"""

    homepage = "https://xgitlab.cels.anl.gov/sds/py-bake"
    url      = "https://xgitlab.cels.anl.gov/sds/py-bake.git"
    git      = "https://xgitlab.cels.anl.gov/sds/py-bake.git"

    version('develop',  branch="master")
    version('0.4', tag='v0.4')
    version('0.3', tag='v0.3')
    version('0.2.1', tag='v0.2.1')
    version('0.2', tag='v0.2')
    version('0.1', tag='v0.1')

    variant('numpy', default=False, description="Enables Numpy support")

    depends_on('py-pybind11', type=('build'))
    depends_on('py-pkgconfig', type=('build'))
    depends_on('bake@0.4:', when='@0.4:')
    depends_on('bake@0.3.1:0.3.6', when='@0.3')
    depends_on('bake@0.1', when='@0.1')
    depends_on('bake@0.3', when='@0.2')
    depends_on('py-margo@0.1:')
    depends_on('py-numpy', when='+numpy')
