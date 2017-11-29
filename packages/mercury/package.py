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


class Mercury(CMakePackage):
    """Mercury is a C library for implementing RPC, optimized for HPC"""

    homepage = "https://mercury-hpc.github.io/"


    version('master', git='https://github.com/mercury-hpc/mercury.git',
            submodules=True)
    # Phil's experimental performance branch
    version('dev-hg-never-block-option', git='https://github.com/carns/mercury.git',
            branch='dev-hg-never-block-option',
            submodules=True)


    variant('cci', default=False, description="Use CCI for network transport")
    variant('bmi', default=False, description="Use BMI for network transport")
    variant('fabric',default=True, description="Use libfabric for net transport")
    variant('selfforward', default=False, description="Mercury will short-circuit operations by forwarding to itself when possible")

    # if nothing specified, build good ol' BMI
    depends_on('cci@master', when="+cci", type=("build", "link", "run"))
    depends_on('libfabric', when="+fabric", type=("build", "link", "run"))
    depends_on('bmi', when="+bmi", type=("build", "link", "run"))
    depends_on('boost')

    def cmake_args(self):
        args = ["-DNA_CCI_USE_POLL:BOOL=ON",
		"-DMERCURY_USE_BOOST_PP:BOOL=ON",
		"-DBUILD_SHARED_LIBS=ON" ]
	if (self.spec.variants['cci'].value):
		args.extend(["-DNA_USE_CCI:BOOL=ON"])
	if (self.spec.variants['bmi'].value):
		args.extend(["-DNA_USE_BMI:BOOL=ON"])
	if (self.spec.variants['fabric'].value):
		args.extend(["-DNA_USE_OFI:BOOL=ON"])
        if (self.spec.variants['selfforward'].value):
                args.extend(["-DMERCURY_USE_SELF_FORWARD=ON"])

        return args
