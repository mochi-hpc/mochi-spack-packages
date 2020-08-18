# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.libfabric import Libfabric

class Libfabric(Libfabric):

    version('1.10.1',
    sha256='889fa8c99eed1ff2a5fd6faf6d5222f2cf38476b24f3b764f2cbb5900fee8284',
        url='https://github.com/ofiwg/libfabric/releases/download/v1.10.1/libfabric-1.10.1.tar.bz2')
    version('1.11.0',
            sha256='9938abf628e7ea8dcf60a94a4b62d499fbc0dbc6733478b6db2e6a373c80d58f',
        url='https://github.com/ofiwg/libfabric/releases/download/v1.11.0/libfabric-1.11.0.tar.bz2', preferred=True)

#            
#    depends_on('m4', when='@1.10.1', type=('build'))
#    depends_on('autoconf', when='@1.10.1', type=('build'))
#    depends_on('automake', when='@1.10.1', type=('build'))
#    depends_on('libtool', when='@1.10.1', type=('build'))
#
#    @when('@1.10.1')
#    def autoreconf(self, spec, prefix):
#        bash = which('bash')
#        bash('./autogen.sh')
#        with working_dir('fabtests'):
#            bash('./autogen.sh')
