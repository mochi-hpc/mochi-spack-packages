from spack import *


class MochiQuintain(AutotoolsPackage):
    """a Mochi microservice for dummy workload benchmarking"""

    homepage = 'https://github.com/mochi-hpc/mochi-quintain/'
    git      = 'https://github.com/mochi-hpc/mochi-quintain.git'

    maintainers = ['carns']

    version('main', branch='main', preferred=True)
    version('develop', branch='main')

    variant('mpi', default=True, description='Build with MPI support')

    depends_on('autoconf', type=("build"))
    depends_on('automake', type=("build"))
    depends_on('libtool', type=("build"))
    depends_on('mpi', when='+mpi')

    # dependencies for normal versions
    depends_on('mochi-bedrock')
    depends_on('json-c')

    # dependencies for develop version
    depends_on('mochi-bedrock@develop', when='@develop')

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
