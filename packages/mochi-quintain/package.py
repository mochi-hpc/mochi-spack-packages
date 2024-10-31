from spack.package import *
from spack import *


class MochiQuintain(AutotoolsPackage):
    """a Mochi microservice for dummy workload benchmarking"""

    homepage = 'https://github.com/mochi-hpc/mochi-quintain/'
    git      = 'https://github.com/mochi-hpc/mochi-quintain.git'
    url      = 'https://github.com/mochi-hpc/mochi-quintain/archive/refs/tags/v0.3.0.tar.gz'

    maintainers = ['carns']

    version('main', branch='main')
    version('develop', branch='main')
    version("0.4.0", sha256="00d05387ebf78627f9c74e68d417066ecc6925c30eaae24cdd1d8fb4e032a20c")
    version("0.3.0", sha256="b72a711f3c5065d73c2ea513f8d7bb266dad48a67428b765826cb4c7cbafdce4")

    variant('mpi', default=True, description='Build with MPI support')

    depends_on('autoconf', type=("build"))
    depends_on('automake', type=("build"))
    depends_on('libtool', type=("build"))
    depends_on('mpi', when='+mpi')

    # dependencies for normal versions
    depends_on('mochi-bedrock@0.15.0:+flock', when='@0.4.0:')
    depends_on('mochi-bedrock@0.14.0:0.14.2+flock', when='@0.3.0')
    depends_on('mochi-flock@0.3.0:+mpi')
    depends_on('json-c')
    depends_on('zlib-api')

    # dependencies for develop version
    depends_on('mochi-bedrock@develop+flock', when='@develop')
    depends_on('mochi-flock@develop+mpi', when='@develop')

    # NOTE: The default autoreconf steps should work fine for this package.
    #       The explicit definition is just here as a workaround; Spack's
    #       default autoreconf step is prone to libtool version mismatch as
    #       of 2021/10/20.
    def autoreconf(self, spec, prefix):
        sh = which('sh')
        sh('./prepare.sh')

    def configure_args(self):
        spec = self.spec
        extra_args = []

        if '+mpi' in spec:
            extra_args.extend([
                "--enable-mpi",
                "CC=%s" % spec['mpi'].mpicc
                ])

        return extra_args
