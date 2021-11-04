# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.mercury import Mercury

class Mercury(Mercury):

    git = 'https://github.com/mercury-hpc/mercury.git'
    version('2.1.0rc3', sha256='e54306cb193c9d9de33688a6f6947b66130ab6b22bbf7ff8f2934cd6801ee081')
    version('2.1.0rc2', sha256='921248fbcaf33ca3fa7d6678982e6132b880a8cc85f20e4c7cbf66508dc0e0be')
    version('2.0.1', sha256='335946d9620ac669643ffd9861a5fb3ee486834bab674b7779eaac9d6662e3fa')
    version('2.0.0',
           sha256='9e80923712e25df56014309df70660e828dbeabbe5fcc82ee024bcc86e7eb6b7')
    version('2.0.0rc1-pvar', git='https://github.com/srini009/mercury.git', branch='mercury_profiling_interface')
    version('master-ucx', branch='ucx', submodules=True)

    variant('ucx', default=False, description='Use UCX plugin')

    depends_on('ucx', when='+ucx')

    def cmake_args(self):
        args = super(Mercury, self).cmake_args()
        spec = self.spec
        variant_bool = lambda feature: str(feature in spec)
        args.append('-DNA_USE_UCX:BOOL=%s' % variant_bool('+ucx'))
        return args
