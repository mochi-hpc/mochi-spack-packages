from spack import *


class MochiBedrock(CMakePackage):
    """Mochi bootstrapping system"""

    homepage = 'https://github.com/mochi-hpc/mochi-bedrock'
    url = 'https://github.com/mochi-hpc/mochi-bedrock/archive/refs/tags/v0.2.1.tar.gz'
    git = 'https://github.com/mochi-hpc/mochi-bedrock.git'

    version('develop', branch='main')
    version('main', branch='main')
    version('master', branch='main')
    version('0.2.1', sha256='cde4f8ecac4d765dba5255d26a5e859460c7f0a2b29dcdffb44866119116ae2c')
    version('0.2', tag='v0.2')
    version('0.1', tag='v0.1')

    depends_on('mochi-margo@0.9:', when='@0.1:9.9.9')
    depends_on('mochi-thallium')
    depends_on('mochi-ssg@0.4.5:', when='@0.1:9.9.9,master,main')
    depends_on('mochi-abt-io')

    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('mochi-margo@develop', when='@develop')
    depends_on('mochi-ssg@develop', when='@develop')
    depends_on('mochi-abt-io@develop', when='@develop')

    depends_on('nlohmann-json')
    depends_on('spdlog')
    depends_on('tclap')

    def cmake_args(self):
        extra_args = ['-DBUILD_SHARED_LIBS=ON']
        return extra_args
