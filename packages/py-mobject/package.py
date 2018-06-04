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
# Installing py-mobject:
#
#     spack install py-mobject
#
from spack import *

class PyMobject(PythonPackage):
    """Python wrapper for the Mobject library"""

    homepage = "https://xgitlab.cels.anl.gov/sds/py-mobject"
    url      = "git@xgitlab.cels.anl.gov:sds/py-mobject.git"

    version('master',  git="git@xgitlab.cels.anl.gov:sds/py-mobject.git")

    depends_on('py-bake')
    depends_on('py-sdskv')
    depends_on('py-margo')
    depends_on('py-ssg+mpi')
    depends_on('mobject')
    depends_on('py-mpi4py')
    depends_on('mpi')
    depends_on('py-pkgconfig', type=('build'))
    depends_on('py-pybind11', type=('build'))
