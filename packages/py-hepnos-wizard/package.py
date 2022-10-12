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


class PyHepnosWizard(PythonPackage):
    """Python utility to help configure the HEPnOS service."""

    homepage = 'https://github.com/hepnos/HEPnOS-Wizard'
    url      = 'https://github.com/hepnos/HEPnOS-Wizard/archive/refs/tags/v0.0.1.tar.gz'
    git      = 'https://github.com/hepnos/HEPnOS-Wizard.git'

    version('develop', branch='main')
    version('main', branch='main')
    version("0.0.2", sha256="ea8dbbaa1066d0e2bafff55a654d18e3439893753a5a068ba868a55c40d4ae23")
    version("0.0.1", sha256="0fc7026e56efad7bad628f26131fba9dbf0c8836ba87ec4f294fdb0b3f2b7bed")

    depends_on('py-setuptools', type=('build'))
    depends_on('py-mochi-bedrock')
