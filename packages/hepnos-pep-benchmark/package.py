from spack import *


class HepnosPepBenchmark(CMakePackage):
    """Parallel event processing benchmark for HEPnOS."""

    homepage = "https://github.com/hepnos/HEPnOS-PEP-Benchmark"
    url = "https://github.com/hepnos/HEPnOS-PEP-Benchmark"
    git = "https://github.com/hepnos/HEPnOS-PEP-Benchmark.git"

    version('develop', branch='main', submodules=True)
    version('main', branch='main', submodules=True)
    version('0.1', branch='main', tag='v0.1', submodules=True, preferred=True)

    depends_on('cmake@3.11.0:', type=('build'))
    depends_on('mpi')
    depends_on('hepnos@0.4:')
    depends_on('tclap')
    depends_on('spdlog')
