from spack import *


class MochiBedrock(CMakePackage):
    """Mochi bootstrapping system"""

    homepage = "https://xgitlab.cels.anl.gov/sds/bedrock"
    url = "https://xgitlab.cels.anl.gov/sds/bedrock"
    git = 'https://xgitlab.cels.anl.gov/sds/bedrock.git'

    version('develop', branch='master')
    version('master', branch='master')
    version('0.1', tag='v0.1', preferred=True)

    depends_on('mochi-margo@0.9:', when='@0.1:9.9.9')
    depends_on('mochi-thallium')
    depends_on('mochi-ssg@master', when='@0.1:9.9.9')
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
