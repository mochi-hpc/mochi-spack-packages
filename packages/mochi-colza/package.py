from spack import *


class MochiColza(CMakePackage):
    """Colza is a Mochi microservice designed to handle an elastic
    staging area for elastic in situ analysis and visualization."""

    homepage = "https://xgitlab.cels.anl.gov/sds/colza"
    url = "https://xgitlab.cels.anl.gov/sds/colza"
    git='https://xgitlab.cels.anl.gov/sds/colza.git'

    version('develop', branch='main')
    version('main', branch='main', preferred=True)

    variant('bedrock', default=True,
            description='Build bedrock module')

    depends_on('mpi')
    depends_on('pkg-config')
    depends_on('nlohmann-json')
    depends_on('spdlog')
    depends_on('tclap')

    depends_on('mochi-thallium @0.8:')
    depends_on('mochi-mona')
    depends_on('mochi-bedrock', when='+bedrock')
    depends_on('mochi-ssg@master', when='@main')

    # dependencies for develop version
    depends_on('mochi-thallium @develop', when='@develop')
    depends_on('mochi-mona @deveop', when='@develop')
    depends_on('mochi-bedrock @develop', when='@develop +bedrock')
    depends_on('mochi-ssg@develop', when='@develop')

    def cmake_args(self):
        args = ['-DBUILD_SHARED_LIBS:BOOL=ON' ]
        if '+bedrock' in self.spec:
            args.append('-DENABLE_BEDROCK=ON')
        else:
            args.append('-DENABLE_BEDROCK=OFF')
        return args
