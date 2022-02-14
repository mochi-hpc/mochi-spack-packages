from spack import *


class MochiColza(CMakePackage):
    """Colza is a Mochi microservice designed to handle an elastic
    staging area for elastic in situ analysis and visualization."""

    homepage = 'https://github.com/mochi-hpc/mochi-colza'
    url = 'https://github.com/mochi-hpc/mochi-colza/archive/refs/tags/v0.1.tar.gz'
    git = 'https://github.com/mochi-hpc/mochi-colza.git'

    version('develop', branch='main')
    version('main', branch='main')
    version('0.1.1', tag='v0.1.1')
    version('0.1', sha256='182c31ebb4d3f0b1b8ac3e8c04daf521d025f9dd981d4728df63f2a12882b2e1')

    variant('bedrock', default=True,
            description='Build bedrock module')
    variant('examples', default=True,
            description='Build colza examples')
    variant('drc', default=False,
            description='Build examples with Cray DRC support')

    depends_on('cmake@3.8:', type='build')
    depends_on('mpi')
    depends_on('pkgconfig')
    depends_on('nlohmann-json')
    depends_on('spdlog')
    depends_on('tclap')

    depends_on('mochi-thallium @0.8:')
    depends_on('mochi-mona')
    depends_on('mochi-bedrock', when='+bedrock')
    depends_on('mochi-ssg @0.4.5', when='@0.1:9.9.9')
    depends_on('mochi-ssg @0.5.2:', when='@main')

    # dependencies for develop version
    depends_on('mochi-thallium @develop', when='@develop')
    depends_on('mochi-mona @develop', when='@develop')
    depends_on('mochi-bedrock @develop', when='@develop +bedrock')
    depends_on('mochi-ssg @develop', when='@develop')

    def cmake_args(self):
        args = ['-DBUILD_SHARED_LIBS:BOOL=ON' ]
        if '+bedrock' in self.spec:
            args.append('-DENABLE_BEDROCK=ON')
        else:
            args.append('-DENABLE_BEDROCK=OFF')
        if '+examples' in self.spec:
            args.append('-DENABLE_EXAMPLES=ON')
        else:
            args.append('-DENABLE_EXAMPLES=OFF')
        if '+drc' in self.spec:
            args.append('-DENABLE_DRC=ON')
        else:
            args.append('-DENABLE_DRC=OFF')

        return args
