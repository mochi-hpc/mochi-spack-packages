from spack import *

class MochiSonata(CMakePackage):
    """Sonata is a Mochi-based document store that uses UnQLite as a backend."""

    homepage = "https://xgitlab.cels.anl.gov/sds/sonata"
    url = "https://xgitlab.cels.anl.gov/sds/sonata"
    git = "https://xgitlab.cels.anl.gov/sds/sonata.git"

    version('master', branch='master')
    version('develop', branch='master')
    version('0.4', tag='v0.4')
    version('0.3', tag='v0.3')
    version('0.2', tag='v0.2')
    version('0.1', tag='v0.1')

    variant('benchmark', default=False, description='Enable building sonata-benchmark')
    variant('daemon', default=True, description='Enable building sonata-daemon')
    variant('unqlite_st', default=True, description='Single-threaded UnQLite')

    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('mochi-thallium')
    depends_on('mochi-thallium@0.7:', when='@0.4:')
    depends_on('unqlite', when='@0.1') # beyond 0.1, unqlite is included in the code
    depends_on('mpi', when='+benchmark')
    depends_on('tclap', type=('build', 'link'))
    depends_on('jsoncpp')
    depends_on('spdlog')
    depends_on('cmake', type=('build'))

    def cmake_args(self):
        args = ['-DBUILD_SHARED_LIBS:BOOL=ON' ]
        if '+benchmark' in self.spec:
            args.append('-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx)
            args.append('-DENABLE_BENCHMARK=ON')
        if '+daemon' in self.spec:
            args.append('-DENABLE_DAEMON=ON')
        if '+unqlite_st' in self.spec:
            args.append('-DENABLE_UNQLITE_THREADS=OFF')
        return args
