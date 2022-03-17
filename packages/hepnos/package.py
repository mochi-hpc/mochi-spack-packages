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

    homepage = "https://github.com/hepnos/HEPnOS"
    url = "https://github.com/hepnos/HEPnOS/archive/v0.4.2.tar.gz"
    git = "https://github.com/hepnos/HEPnOS.git"


    version('0.6.4', sha256='86558a700144abc7ffa2ba8f2b3963e16f97c175e80f6a004c34dfa6b4b6f564')
    version('0.6.3', sha256='b1e7b5ebd159771cc0f0cec08d76d563ee831fba82c5aa5ea92078b22fe34fc1')
    version('0.6.2', sha256='83a96f3f438aacf01c2d4e917726bd3b1911dbb4f824517bebfbf15d8ea0bdd6')
    version('0.6.1', sha256='13ca7c6ff5616db64b44bb962654efbb41cb86343681453048106b29521575c4')
    version('0.6', sha256='b3091114fabedac6683867114e9a4f603ba8de451d4c93eec933232c70f87521')
    version('0.5', sha256='42b58f0b7c9268ab8411f353da276835f0627ae38853ebb9ab709c9b36a75d06')
    version('0.4.6', sha256='930012cbc684565c98b69e38bb5485eed042d4e406712e14d90ee8e284d7cc4e')
    version('0.4.5', sha256='bd36e6b8e468d161be59a39765c7f9bd98f9a9cc5c5a3413d05ca01e6997be54')
    version('0.4.4', sha256='3782151f637927f739ae69d46aee2ea9b1cb169b53fe2557ea8b27ae849dbb7d')
    version('0.4.3', sha256='6a93ff41d7bd606e0c30c9e91d88c102ecccda354a856448405a151c82e5f81c')
    version('0.4.2', sha256='8ffe661ed6345c682f4328973db879aa00a4a2c6154decdb86675f5f6e6476d9')
    version('0.4.1', sha256='d6c713178dcb82253d0c1ce9ccc3fb7101262fb6ddcf8f25243de05ab996cb04')
    version('0.4.0', sha256='c3ea8163b768a7c69ca171c340561a2c27eff78aef958b5d44c16af5293a8220')
    version('0.3.2', sha256='59ce5a274f95bfe98a5cff7bd2c4b89342ee44a101e7fb1aed91f2a8652c97d6')
    version('0.3.1', sha256='9229ab6affdd6c084e4316690deff0b2ddb630e64bc6801bcfe6fe2e4c976a10')
    version('0.3.0', sha256='629454336dbd4ab9eeceaff345933657a1406760c1565028c51efb461cd62358')
    version('0.2.0', sha256='6a675d37540b59a581beba6e35f924e92f171facbd129cf89aa58181473f4ae4')
    version('0.1.8', sha256='3d1bb419413dbef502e69f13509fe4ec2f736590e9ac20a3f0755e348b3ac11e')
    version('0.1.7', sha256='42095ec0f28a5fbd41ebafba5cce71f961b8d06c23bf6a5cc5ca786b05989cf2')
    version('0.1.6', tag='v0.1.6')
    version('0.1.5', tag='v0.1.5')
    version('0.1.4', tag='v0.1.4')
    version('0.1.3', tag='v0.1.3')
    version('0.1.2', tag='v0.1.2')
    version('0.1.1', tag='v0.1.1')
    version('0.1',   tag='v0.1')
    version('develop', branch='main')
    version('main', branch='main')

    variant('cxxstd',
            default='14',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    # ---------------------------------------------
    # Non-mochi dependencies
    # ---------------------------------------------
    depends_on('mpi')
    depends_on('spdlog')
    depends_on('boost+serialization')
    depends_on('cmake@3.12.0:')
    depends_on('uuid', when='@0.5:')
    depends_on('nlohmann-json', when='@0.5:')
    # ---------------------------------------------
    # Current mochi dependencies
    # ---------------------------------------------
    depends_on('mochi-ch-placement@0.1:')
    depends_on('mochi-thallium@0.5.2:', when='@0.2.0:')
    depends_on('mochi-bedrock+mpi', when='@0.5:')
    depends_on('mochi-yokan+bedrock@0.2.1:', when='@0.6:')
    # ---------------------------------------------
    # Dependencies for develop version
    # ---------------------------------------------
    depends_on('mochi-ch-placement@develop', when='@develop')
    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('mochi-yokan+bedrock@develop', when='@develop')
    depends_on('mochi-bedrock+mpi@develop', when='@develop')
    # ---------------------------------------------
    # Old dependencies
    # ---------------------------------------------
    depends_on('yaml-cpp@develop', when='@:0.4.6')
    depends_on('libuuid', when='@0.2.0:0.4.6')
    depends_on('mochi-margo@0.5.2:', when='@0.1.8')
    depends_on('mochi-sdskv@0.1.10:', when='@0.3.1:0.5')
    depends_on('mochi-sdskv@0.1.8:', when='@0.2.0:0.5')
    depends_on('mochi-sdskv@0.1.7:', when='@0.1.8:0.5')
    depends_on('mochi-sdskv@0.1:', when='@:0.5')
    depends_on('mochi-bake@0.1:0.3.6', when='@:0.1.7')

    def cmake_args(self):
        extra_args = ['-DBUILD_SHARED_LIBS=ON']
        extra_args.extend(['-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx])
        extra_args.extend(['-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value])
        return extra_args
