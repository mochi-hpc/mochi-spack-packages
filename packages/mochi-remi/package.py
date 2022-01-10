from spack import *


class MochiRemi(CMakePackage):
    """REMI is a Mochi microservice designed to handle the migration of sets of files
    from a node to another. It uses RDMA and memory mapping to efficiently transfer
    potentially large groups of files at once."""

    homepage = 'https://github.com/mochi-hpc/mochi-remi'
    url = 'https://github.com/mochi-hpc/mochi-remi'
    git = 'https://github.com/mochi-hpc/mochi-remi.git'

    version('develop', branch='main')
    version('main', branch='main')
    version('0.3.1', tag='v0.3.1')
    version('0.3', tag='v0.3')
    version('0.2.3', tag='v0.2.3')
    version('0.2.2', tag='v0.2.2')
    version('0.2.1', tag='v0.2.1')
    version('0.2', tag='v0.2')
    version('0.1.1', tag='v0.1.1')
    version('0.1', tag='v0.1')

    variant('bedrock', default=True, description='Enable building Bedrock module')

    depends_on('cmake@3.12:', type='build')
    depends_on('libuuid')
    depends_on('mochi-thallium@0.6.0:+cereal', when='@0.2.3:')
    depends_on('mochi-thallium@0.4.2:', when='@0.2.2')
    depends_on('mochi-thallium@0.3:', when='@:0.2.1')
    depends_on('mochi-abt-io@0.1:')
    depends_on('mochi-bedrock@0.2:', when='@0.3: +bedrock')

    # dependencies for develop version
    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('mochi-abt-io@develop', when='@develop')
    depends_on('mochi-bedrock@develop', when='@develop +bedrock')

    patch('0001-explicitly-request-C-14.patch')

    conflicts('+bedrock', when='@:0.2.3',
              msg='+bedrock variant only available starting from 0.3')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON" ]
        if '+bedrock' in self.spec:
            args.append('-DENABLE_BEDROCK=ON')
        else:
            args.append('-DENABLE_BEDROCK=OFF')
        return args
