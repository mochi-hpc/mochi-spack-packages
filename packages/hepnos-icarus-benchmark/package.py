from spack.package import *
from spack import *


class HepnosIcarusBenchmark(CMakePackage):
    """Benchmark for HEPnOS that mimics the ICARUS application."""

    homepage = "https://github.com/hepnos/HEPnOS-ICARUS-Benchmark"
    url = "https://github.com/hepnos/HEPnOS-ICARUS-Benchmark"
    git = "https://github.com/hepnos/HEPnOS-ICARUS-Benchmark.git"

    version('develop', branch='main')
    version('main', branch='main', preferred=True)

    depends_on('cmake@3.11.0:', type=('build'))
    depends_on('mpi')
    depends_on('hepnos@0.6.6:')
    depends_on('tclap')
    depends_on('spdlog')

    def cmake_args(self):
        extra_args = ['-DBUILD_SHARED_LIBS=ON',
                      '-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx]
        return extra_args
