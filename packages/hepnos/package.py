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


class Hepnos(CMakePackage):
    """Object store for High Energy Physics, build around Mochi components"""

    homepage = "https://xgitlab.cels.anl.gov/sds/HEPnOS"
    url = "https://xgitlab.cels.anl.gov/sds/HEPnOS"

    version('0.1', git='https://xgitlab.cels.anl.gov/sds/HEPnOS.git', tag='v0.1')
    version('master', git='https://xgitlab.cels.anl.gov/sds/HEPnOS.git')

    depends_on('mpi')
    depends_on('ch-placement')
    depends_on('sdskeyval')
    depends_on('bake')
    depends_on('yaml-cpp@develop')
    depends_on('boost+serialization')

    def cmake_args(self):
        extra_args = []
        extra_args.extend(['-DCMAKE_CC_COMPILER=%s'  % self.spec['mpi'].mpicc])
        extra_args.extend(['-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx])
        return extra_args
