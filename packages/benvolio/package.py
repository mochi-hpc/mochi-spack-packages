# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
from spack import *


class Benvolio(AutotoolsPackage):
    """Mochi services for I/O"""

    homepage = "https://github.com/mochi-hpc/benvolio"
    url      = "https://github.com/mochi-hpc/benvolio"
    git      = "https://github.com/mochi-hpc/benvolio.git"

    version('main', branch='main', preferred=True)
    version('develop', branch='main')

    variant('mpi', default=False, description='Bootstrap Benvolio providers with MPI');
    variant('pmix', default=True, description='Bootstrap Benvolio providers with PMIx');
    variant('cray-drc', default=False, description='Use Cray Dynamic RDMA Credientials');

    depends_on('automake')
    depends_on('autoconf')
    depends_on('libtool')
    # thallium-0.5 provided engine::wrap()
    # thallim-0.8.2 provided an engine constructor that takes margo hints
    depends_on('mochi-thallium@0.8.2:')
    depends_on('mochi-abt-io@0.2:')
    # pick up ssg API rework that landed in ssg-0.4.0
    # can bootstrap with either pmix or mpi.. not sure how to specify that in spack
    depends_on('mochi-ssg@0.4.0:+pmix', when='+pmix')
    depends_on('mochi-ssg@0.4.0:+mpi', when='+mpi')
    depends_on('rdma-credentials', when='+cray-drc')

    # @develop version
    #depends_on('mochi-thallium@develop', when='@develop')
    #depends_on('mochi-ssg+mpi@develop', when='@develop')

    # NOTE: The default autoreconf steps should work fine for this package.
    #       The explicit definition is just here as a workaround; Spack's
    #       default autoreconf step is prone to libtool version mismatch as
    #       of 2021/10/20.
    def autoreconf(self, spec, prefix):
        sh = which('sh')
        sh('-c', 'autoreconf -fi')

    # Require a custom configure_args if we need to build with MPI wrapper

    def configure_args(self):
        extra_args = []
        if '+mpi' in self.spec:
            extra_args.extend(['CC=%s' % self.spec['mpi'].mpicc])
            extra_args.extend(['CXX=%s' % self.spec['mpi'].mpicxx])

        return extra_args
