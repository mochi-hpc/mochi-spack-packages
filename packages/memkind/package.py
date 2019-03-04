# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install memkind
#
# You can edit this file again by typing:
#
#     spack edit memkind
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Memkind(AutotoolsPackage):
    """The memkind library is a user extensible heap manager built on top of
    jemalloc which enables control of memory characteristics and a partitioning
    of the heap between kinds of memory."""

    homepage = "http://memkind.github.io/memkind/"
    url      = "https://github.com/memkind/memkind/archive/v1.8.0.tar.gz"

    version('1.8.0', sha256='8b57c5afa8afa6793e4662322e37620bbb11f119cd8d29654ec00945bbe13a17')
    version('1.7.0', sha256='5048eaaa1bc484203c685a019f3f428ab6c9b1cf94ef6d264e299bc0127ec572')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('numactl', type=('build', 'link'))

    @run_before('autoreconf')
    def bootstrap(self):
        bash = which('bash')
        bash('./build_jemalloc.sh')

    def autoreconf(self, spec, path):
        bash = which('bash')
        bash('./autogen.sh')

    # 'configure_args' function not needed
