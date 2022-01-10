from spack import *


class MochiBedrock(CMakePackage):
    """Mochi bootstrapping system"""

    homepage = 'https://github.com/mochi-hpc/mochi-bedrock'
    url = 'https://github.com/mochi-hpc/mochi-bedrock/archive/refs/tags/v0.2.1.tar.gz'
    git = 'https://github.com/mochi-hpc/mochi-bedrock.git'

    version('develop', branch='main')
    version('main', branch='main')
    version('0.3.3', sha256='aca8f197ffd093327daafa872fe090641de96079e57bd0accb51d21cc0897125')
    version('0.3.2', sha256='d71697996107c708716d03264b401368bfb4e2b7500ebc550fba99e4ce19200d')
    version('0.3.1', sha256='8cec65c1924477434dfb5172af611bcc2641c2b37f3570018ccba2a2c7d87251')
    version('0.3', sha256='49a4ff559ced96826eff681f601a67edf9a431f3549403abe0d2c5f849222ae6')
    version('0.2.3', sha256='da29cd1522aeba373149f43ea4e2a9ea2a425132b1d43e7b7e9e485f38699f7f')
    version('0.2.2', sha256='fa938f6a2349037c485f81c5258a5b72a839683e6ec1363a6cf9a0f7a2ba9e5e')
    version('0.2.1', sha256='cde4f8ecac4d765dba5255d26a5e859460c7f0a2b29dcdffb44866119116ae2c')
    version('0.2', tag='v0.2')
    version('0.1', tag='v0.1')

    variant('mpi', default=False, description='Enable MPI bootstrapping')

    depends_on('mochi-margo@0.9:')
    depends_on('mochi-thallium')
    depends_on('mochi-abt-io')
    # SSG dependencies for versions up to 0.3
    depends_on('mochi-ssg@0.4.5', when='@0.1.0:0.3.0')
    depends_on('mochi-ssg+mpi@0.4.5', when='@0.1.0:0.3.0 +mpi')
    # SSG dependencies for versions up to 0.3.2
    depends_on('mochi-ssg@0.4.6', when='@0.3.1:0.3.2')
    depends_on('mochi-ssg+mpi@0.4.6', when='@0.3.1:0.3.2 +mpi')
    # SSG dependencies for version >= 0.3.3
    depends_on('mochi-ssg@0.5:', when='@0.3.3:')
    depends_on('mochi-ssg+mpi@0.5:', when='@0.3.3: +mpi')

    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('mochi-margo@develop', when='@develop')
    depends_on('mochi-ssg@develop', when='@develop')
    depends_on('mochi-ssg+mpi@develop', when='@develop +mpi')
    depends_on('mochi-abt-io@develop', when='@develop')

    depends_on('mpi', when='+mpi')

    depends_on('cmake@3.8:', type='build')
    depends_on('nlohmann-json')
    depends_on('spdlog')
    depends_on('tclap')

    def cmake_args(self):
        extra_args = ['-DBUILD_SHARED_LIBS=ON']
        if '+mpi' in self.spec:
            extra_args.append('-DENABLE_MPI=ON')
            extra_args.append('-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx)
        else:
            extra_args.append('-DENABLE_MPI=OFF')
        return extra_args
