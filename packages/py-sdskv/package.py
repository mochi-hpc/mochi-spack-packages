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
# Installing py-sdskv:
#
#     spack install py-sdskv
#
from spack import *

class PySdskv(PythonPackage):
    """Python wrapper for the SDS-KeyVal library"""

    homepage = "https://xgitlab.cels.anl.gov/sds/py-sdskv"
    url      = "https://xgitlab.cels.anl.gov/sds/py-sdskv.git"

    version('master',  git="https://xgitlab.cels.anl.gov/sds/py-sdskv.git")
    version('provider',  git="https://xgitlab.cels.anl.gov/sds/py-sdskv.git", branch='dev-provider-id')

    depends_on('sdskeyval', when='@master')
    depends_on('py-margo', when='@master')
    depends_on('py-pkgconfig')
    depends_on('sdskeyval@provider', when='@provider')
    depends_on('py-margo@provider', when='@provider')
