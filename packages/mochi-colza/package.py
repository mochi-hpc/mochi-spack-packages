from spack import *


class MochiColza(CMakePackage):
    """Colza is a Mochi microservice designed to handle an elastic
    staging area for elastic in situ analysis and visualization."""

    homepage = 'https://github.com/mochi-hpc/mochi-colza'
    url = 'https://github.com/mochi-hpc/mochi-colza/archive/refs/tags/v0.1.tar.gz'
    git = 'https://github.com/mochi-hpc/mochi-colza.git'

    version('develop', branch='main')
    version('main', branch='main')
    version('0.2.1', sha256='0c4e8d96a4e147705835c674182a8c23e0429587343331bd21e09cc63365f853')
    version('0.2.0', sha256='5a9de73cdcb7e8e66325143741fde756346362ee84217ff308674827a11029c7')
    version('0.1.3', sha256='af339244676916658bcb305d57836b576ea55def61cfb3efd323694922eb7613')
    version('0.1.2', sha256='40a78dc5a455608641a399e1f6c397d02dc730c6a81340233ad42aad691dda92')
    version('0.1.1', sha256='fcbb09ebb3c1e566c608918feb8371cc6fbf2c992e73fa3b8eddd77abc26055f')
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
    depends_on('mochi-bedrock @0.5.0: +ssg +mona', when='@0.2.0: +bedrock')
    depends_on('mochi-ssg @0.4.5', when='@0.1:0.1.1')
    depends_on('mochi-ssg @0.5.2:', when='@main,0.1.2:')

    # dependencies for develop version
    depends_on('mochi-thallium @develop', when='@develop')
    depends_on('mochi-mona @develop', when='@develop')
    depends_on('mochi-bedrock+ssg+mona @develop', when='@develop +bedrock')
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
