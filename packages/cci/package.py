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
# to execute our custom autoreconf script
from subprocess import call



class Cci(AutotoolsPackage):
    """A simple, portable, high-performance, scalable, and robust communication
    interface for HPC and Data Centers."""

    homepage = "http://cci-forum.com/"
    url      = "http://cci-forum.com/wp-content/uploads/2016/06/cci-2.0.tar.gz"

    depends_on('m4', type='build', when='@master');
    depends_on('autoconf', type='build', when='@master');
    depends_on('automake', type='build', when='@master');
    depends_on('libtool', type='build', when='@master');

    patch('0001-Werror-is-a-little-aggressive.patch');

    version('master', git='https://github.com/CCI/cci.git')
    version('2.0', '070b2ba4eca92a846c093f2cd000d3b2')
    def configure_args(self):
        # TODO: need variants for verbs and ugni
            args = ['--without-gni',
                    '--without-verbs',
                    '--disable-picky'
]
            return args

    # need to override 'autoreconf' so we can run CCI's 'autogen.pl' script
    def autoreconf(self, spec, prefix):
        with working_dir(self.configure_directory):
                call("./autogen.pl");
