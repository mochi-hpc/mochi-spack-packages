from spack import *

class MochiXferBenchmark(CMakePackage):
    """A benchmark testing various data transfer strategies for Mochi."""

    homepage = 'https://github.com/mochi-hpc-experiments/mochi-xfer-benchmark'
    git = 'https://github.com/mochi-hpc-experiments/mochi-xfer-benchmark.git'

    version('main', branch='main', preferred=True)
    version('develop', branch='main')

    depends_on('pkgconfig', type=('build'))
    depends_on('tclap', type=('build'))
    depends_on('mochi-thallium')
    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('spdlog')
    depends_on('mpi')
