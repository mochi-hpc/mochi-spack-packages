from spack import *


class HepnosPepBenchmark(CMakePackage):
    """Parallel event processing benchmark for HEPnOS."""

    homepage = "https://xgitlab.cels.anl.gov/sds/hep/HEPnOS-PEP-Benchmark"
    url = "https://xgitlab.cels.anl.gov/sds/hep/HEPnOS-PEP-Benchmark"
    git = 'https://xgitlab.cels.anl.gov/sds/hep/HEPnOS-PEP-Benchmark.git'

    version('develop', branch='master', submodules=True)
    version('master', branch='master', submodules=True)
    version('0.1', branch='master', tag='v0.1', submodules=True, preferred=True)

    depends_on('cmake@3.11.0:', type=('build'))
    depends_on('mpi')
    depends_on('hepnos@0.4:')
    depends_on('tclap')
    depends_on('spdlog')
