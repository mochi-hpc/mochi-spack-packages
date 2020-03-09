# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
from spack import *


class Benvolio(AutotoolsPackage):
    """Mochi services for I/O"""

    homepage = "https://xgitlab.cels.anl.gov/sds/benvolio"
    url      = "https://xgitlab.cels.anl.gov/sds/benvolio"
    git      = "https://xgitlab.cels.anl.gov/sds/benvolio.git"

    version('master', branch='master', preferred=True)
    version('develop', branch='master')

    depends_on('automake')
    depends_on('autoconf')
    depends_on('libtool')
    # thallium-0.5 provided engine::wrap()
    depends_on('mochi-thallium@0.5:')
    depends_on('mochi-abt-io@0.2:')
    # pick up ssg API rework that landed in ssg-0.4.0
    depends_on('mochi-ssg+mpi@0.4.0:')

    # @develop version
    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('mochi-ssg+mpi@develop', when='@develop')

    def configure_args(self):
        extra_args = []
        extra_args.extend(['CC=%s' % self.spec['mpi'].mpicc])
        extra_args.extend(['CXX=%s' % self.spec['mpi'].mpicc])
        return extra_args
