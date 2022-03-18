from spack import *


class HepnosPepBenchmark(CMakePackage):
    """Parallel event processing benchmark for HEPnOS."""

    homepage = "https://github.com/hepnos/HEPnOS-PEP-Benchmark"
    url = "https://github.com/hepnos/HEPnOS-PEP-Benchmark"
    git = "https://github.com/hepnos/HEPnOS-PEP-Benchmark.git"

    version('develop', branch='main', submodules=True)
    version('main', branch='main', submodules=True)
    version('0.6', tag='v0.6', submodules=True)
    version('0.5', tag='v0.5', submodules=True)
    version('0.4', tag='v0.4', submodules=True)
    version('0.3', tag='v0.3', submodules=True)
    version('0.2', tag='v0.2', submodules=True)
    version('0.1', tag='v0.1', submodules=True)

    variant("classes", default="test", description="Which set of classes to build",
            values=('test', 'all'), multi=False)

    depends_on('cmake@3.11.0:', type=('build'))
    depends_on('mpi')
    depends_on('hepnos@0.6:', when='@0.5:')
    depends_on('hepnos@0.5', when='@0.4')
    depends_on('hepnos@0.4:0.5', when='@:0.4')
    depends_on('hepnos@:0.4.6', when='@:0.3')
    depends_on('tclap')
    depends_on('spdlog@:1.8.0') # TODO fix HEPnOS serialization so 1.8.1+ work

    def cmake_args(self):
        extra_args = ['-DBUILD_SHARED_LIBS=ON']
        extra_args.extend(['-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx])
        if self.spec.variants['classes'].value == 'test':
            extra_args.extend(['-DONLY_TEST_CLASSES=ON'])
        return extra_args
