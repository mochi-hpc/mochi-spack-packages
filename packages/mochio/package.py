# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
from spack import *


class Mochio(AutotoolsPackage):
    """Mochi services for I/O"""

    homepage = "https://xgitlab.cels.anl.gov/sds/mochio"
    url      = "https://xgitlab.cels.anl.gov/sds/mochio"
    git      = "https://xgitlab.cels.anl.gov/sds/mochio.git"

    version('develop', branch='master')

    depends_on('automake')
    depends_on('autoconf')
    depends_on('libtool')
    depends_on('thallium@0.3.4:')
    depends_on('abt-io@0.2:')
    depends_on('ssg+mpi@0.2:')

    def configure_args(self):
        extra_args = []
        extra_args.extend(['CC=%s' % self.spec['mpi'].mpicc])
        extra_args.extend(['CXX=%s' % self.spec['mpi'].mpicc])
        return extra_args
