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


class MochiMargo(AutotoolsPackage):
    """A library that provides Argobots bindings to the Mercury RPC
    implementation."""

    homepage = 'https://xgitlab.cels.anl.gov/sds/margo'
    git = 'https://xgitlab.cels.anl.gov/sds/margo.git'

    version('develop', branch='master')
    version('0.6.3', tag='v0.6.3')
    version('0.6.2', tag='v0.6.2')
    version('0.6.1', tag='v0.6.1')
    version('0.6', tag='v0.6')
    version('0.5.2', tag='v0.5.2')
    version('0.5.1', tag='v0.5.1')
    version('0.5',   tag='v0.5')
    version('0.4.7', tag='v0.4.7')
    version('0.4.6', tag='v0.4.6')
    version('0.4.5', tag='v0.4.5')
    version('0.4.4', tag='v0.4.4')
    version('0.4.3', tag='v0.4.3')
    version('0.4.2', tag='v0.4.2')

    # RPC breadcrubmb support introduced in margo-0.5.2 requires latest mercury
    # (until mercury has a release we can track
    depends_on('mercury@1.0.0:', type=("build", "link", "run"), when='@:0.5.1')
    depends_on('mercury@2.0.0a1:', type=("build", "link", "run"), when='@0.5.2:')
    depends_on('argobots@1.0rc2:')
    depends_on('autoconf@2.65:', type=("build"))
    depends_on('m4', type=('build'))
    depends_on('automake', type=("build"))
    depends_on('libtool', type=("build"))
    depends_on('pkg-config', type=("build"))
