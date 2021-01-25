# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class MochiMargo(AutotoolsPackage):
    """A library that provides Argobots bindings to the Mercury RPC
    implementation."""

    homepage = 'https://xgitlab.cels.anl.gov/sds/margo'
    git = 'https://xgitlab.cels.anl.gov/sds/margo.git'

    maintainers = ['carns', 'mdorier']

    version('master', branch='master')
    version('develop', branch='master')
    version('0.9', tag='v0.9')
    version('0.7.2', tag='v0.7.2')
    version('0.7.1', tag='v0.7.1')
    version('0.7', tag='v0.7')
    version('0.6.4', tag='v0.6.4')
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

    depends_on('json-c', when='@0.9:')
    depends_on('autoconf@2.65:', type=("build"))
    depends_on('m4', type=('build'))
    depends_on('automake', type=("build"))
    depends_on('libtool', type=("build"))
    depends_on('pkgconfig', type=("build"))
    depends_on('argobots@1.0:')
    # "breadcrumb" support not available in mercury-1.0
    depends_on('mercury@1.0.0:', type=("build", "link", "run"), when='@:0.5.1')
    depends_on('mercury@2.0.0:', type=("build", "link", "run"), when='@0.5.2:')

    # dependencies for develop version
    depends_on('mercury@master', type=("build", "link", "run"), when='@develop')
