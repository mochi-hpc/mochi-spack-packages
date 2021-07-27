# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.mercury import Mercury

class Mercury(Mercury):

    git = 'https://github.com/mercury-hpc/mercury.git'
    version('2.0.1', sha256='335946d9620ac669643ffd9861a5fb3ee486834bab674b7779eaac9d6662e3fa')
    version('2.0.0',
           sha256='9e80923712e25df56014309df70660e828dbeabbe5fcc82ee024bcc86e7eb6b7')
    version('2.0.0rc1-pvar', git='https://github.com/srini009/mercury.git', branch='mercury_profiling_interface')
    version('master-ucx', branch='ucx', submodules=True)

    variant('ucx', default=False, description='Use UCX plugin')

    depends_on('ucx', when='+ucx')

    def cmake_args(self):
        """Populate cmake arguments for Mercury."""
        spec = self.spec
        variant_bool = lambda feature: str(feature in spec)
        parallel_tests = '+mpi' in spec and self.run_tests

        cmake_args = [
            '-DBUILD_SHARED_LIBS:BOOL=%s' % variant_bool('+shared'),
            '-DBUILD_TESTING:BOOL=%s' % str(self.run_tests),
            '-DMERCURY_ENABLE_PARALLEL_TESTING:BOOL=%s' % str(parallel_tests),
            '-DMERCURY_USE_BOOST_PP:BOOL=ON',
            '-DMERCURY_USE_CHECKSUMS:BOOL=%s' % variant_bool('+checksum'),
            '-DMERCURY_USE_SYSTEM_MCHECKSUM:BOOL=OFF',
            '-DMERCURY_USE_XDR:BOOL=OFF',
            '-DNA_USE_UCX:BOOL=%s' % variant_bool('+ucx'),
            '-DNA_USE_BMI:BOOL=%s' % variant_bool('+bmi'),
            '-DNA_USE_CCI:BOOL=%s' % variant_bool('+cci'),
            '-DNA_USE_MPI:BOOL=%s' % variant_bool('+mpi'),
            '-DNA_USE_SM:BOOL=%s'  % variant_bool('+sm'),
        ]

        if '@2.0.0:' in spec:
            cmake_args.extend([
                '-DMERCURY_ENABLE_DEBUG:BOOL=%s' % variant_bool('+debug'),
            ])

        # Previous versions of mercury had more extensive CMake options
        if '@:1.0.1' in spec:
            cmake_args.extend([
                '-DMERCURY_ENABLE_POST_LIMIT:BOOL=OFF',
                '-DMERCURY_ENABLE_VERBOSE_ERROR=%s' % variant_bool('+debug'),
                '-DMERCURY_USE_EAGER_BULK:BOOL=ON',
                '-DMERCURY_USE_SELF_FORWARD:BOOL=ON',
            ])

        if '@1.0.0:' in spec:
            cmake_args.extend([
                '-DMERCURY_USE_SYSTEM_BOOST:BOOL=%s'
                % variant_bool('+boostsys'),
                '-DNA_USE_OFI:BOOL=%s' % variant_bool('+ofi'),
            ])

        if '+ofi' in spec:
            cmake_args.append(
                '-DNA_OFI_GNI_USE_UDREG:BOOL=%s' % variant_bool('+udreg')
            )
            if self.run_tests:
                cmake_args.append(
                    '-DNA_OFI_TESTING_PROTOCOL:STRING={0}'.format(
                        ';'.join(spec['libfabric'].variants['fabrics'].value)
                    )
                )

        return cmake_args
