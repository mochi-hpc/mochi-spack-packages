# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.libfabric import Libfabric

class Libfabric(Libfabric):

    version('1.9.1',
    sha256='c305c6035c992523e08c7591a6a3707225ba3e72de40443eaed837a10df6771a',
        url='https://github.com/ofiwg/libfabric/releases/download/v1.9.1/libfabric-1.9.1.tar.bz2', preferred=True)
    version('1.10.rc1', tag='v1.10.0rc1')
    depends_on('m4', when='@1.10.rc1', type=('build'))
    depends_on('autoconf', when='@1.10.rc1', type=('build'))
    depends_on('automake', when='@1.10.rc1', type=('build'))
    depends_on('libtool', when='@1.10.rc1', type=('build'))

    @when('@1.10.rc1')
    def autoreconf(self, spec, prefix):
        bash = which('bash')
        bash('./autogen.sh')
        with working_dir('fabtests'):
            bash('./autogen.sh')

