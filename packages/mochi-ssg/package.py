from spack import *


class MochiSsg(AutotoolsPackage):
    """A Mochi group membership microservice.
    It provides mechanisms for bootstrapping sets of Mochi processes into
    logical groups and for managing the membership of these process groups over
    time. At a high-level, each group collectively maintains a group view,
    which is just a mapping from group member identifiers to Mercury address
    information"""

    homepage = 'https://github.com/mochi-hpc/mochi-ssg'
    git = 'https://github.com/mochi-hpc/mochi-ssg.git'
    url = 'https://github.com/mochi-hpc/mochi-ssg/archive/v0.2.tar.gz'

    maintainers = ['shanedsnyder']

    version('main', branch='main')
    version('develop', branch='main')
    version('dev-error-codes', branch='dev-error-codes')
    version('0.5.2', tag='v0.5.2')
    version('0.5.1', tag='v0.5.1')
    version('0.5.0', tag='v0.5.0')
    version('0.4.6', tag='v0.4.6')
    version('0.4.5', tag='v0.4.5')
    version('0.4.4', tag='v0.4.4')
    version('0.4.3.1', tag='v0.4.3.1')
    version('0.4.2', tag='v0.4.2')
    version('0.4.1', tag='v0.4.1')
    version('0.4.0', tag='v0.4.0')
    version('0.3.0', tag='v0.3.0')
    version('0.2', tag='v0.2')

    patch('0001-additional-error-reporting.patch', when='@0.2')
    patch('0001-Add-an-explicit-check-for-pmix-libs.patch', when='@0.4.1')
    patch('0001-Improve-deserialize-error-reporting.patch', when='@0.4.1')
    patch('0001-WIP-TIMEOUT-instead-of-IMMEDIATE.patch', when='@0.4.0:')

    variant('valgrind', default=False, description='Build a Valgrind-friendly SSG')
    variant('mpi', default=True, description='Build with MPI support')
    variant('pmix', default=False, description='Build with PMIx support')
    variant('drc', default=False, description='Support Cray Dynamic RDMA Credentials')

    depends_on('mpi', when='+mpi')
    depends_on('pmix', when='+pmix')
    depends_on('rdma-credentials', when="+drc")

    depends_on('autoconf@2.69:', type=('build'))
    depends_on('m4', type=('build'))
    depends_on('automake', type=("build"))
    depends_on('libtool', type=("build"))
    depends_on('pkgconfig', type=("build"))

    depends_on('mochi-margo@0.4:')
    depends_on('mochi-margo@0.6:', when='@0.4.1:')
    depends_on('mochi-margo@develop', when='@develop')

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

        if '+pmix' in spec:
            extra_args.extend([
                "--enable-pmix"
                ])
        else:
            extra_args.extend([
                "--disable-pmix"
                ])

        if '+drc' in spec:
            extra_args.extend([
                "--enable-drc"
            ])

        if '+valgrind' in spec:
            extra_args.extend([
                "--enable-valgrind"
            ])

        return extra_args

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
