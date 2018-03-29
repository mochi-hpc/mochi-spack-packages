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


class Margo(AutotoolsPackage):
    """a library that provides Argobots bindings to the Mercury RPC
    implementation."""

    homepage = "https://xgitlab.cels.anl.gov/sds/margo"

    version('master', git='https://xgitlab.cels.anl.gov/sds/margo.git')
    version('margo-registered-data',
            git='https://xgitlab.cels.anl.gov/sds/margo.git',
            branch='margo-registered-data')

    version('provider', git='https://xgitlab.cels.anl.gov/sds/margo.git',
		    branch='dev-provider-id')

    depends_on('mercury@pre-scalable-ep', when='@master', type=("build", "link", "run"))
    depends_on('mercury@provider', when='@provider', type=("build", "link", "run"))
    depends_on('argobots')
    depends_on('abtsnoozer')
    depends_on('libev')
    depends_on('autoconf@2.65:')
    depends_on('automake', type=("build"))
    depends_on('libtool', type=("build"))
    # 'timeout' is part of coreutils
    depends_on('coreutils')
    depends_on('pkg-config')
