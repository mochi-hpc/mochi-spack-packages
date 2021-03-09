from spack import *


class MochiColza(CMakePackage):
    """Colza is a Mochi microservice designed to handle an elastic
    staging area for elastic in situ analysis and visualization."""

    homepage = 'https://github.com/mochi-hpc/mochi-colza'
    url = 'https://github.com/mochi-hpc/mochi-colza'
    git = 'https://github.com/mochi-hpc/mochi-colza.git'

    version('develop', branch='main')
    version('main', branch='main', preferred=True)

    variant('bedrock', default=True,
            description='Build bedrock module')
    variant('examples', default=True,
            description='Build colza examples')
    variant('drc', default=True,
            description='Build examples with Cray DRC support')

    depends_on('mpi')
    depends_on('pkgconfig')
    depends_on('nlohmann-json')
    depends_on('spdlog')
    depends_on('tclap')

    depends_on('mochi-thallium @0.8:')
    depends_on('mochi-mona')
    depends_on('mochi-bedrock', when='+bedrock')
    depends_on('mochi-ssg@master', when='@main')

    # dependencies for develop version
    depends_on('mochi-thallium @develop', when='@develop')
    depends_on('mochi-mona @develop', when='@develop')
    depends_on('mochi-bedrock @develop', when='@develop +bedrock')
    depends_on('mochi-ssg@develop', when='@develop')

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
