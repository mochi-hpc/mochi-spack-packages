from spack import *


class MochiSsg(AutotoolsPackage):
    """A Mochi group membership microservice.
    It provides mechanisms for bootstrapping sets of Mochi processes into
    logical groups and for managing the membership of these process groups over
    time. At a high-level, each group collectively maintains a group view,
    which is just a mapping from group member identifiers to Mercury address
    information"""

    homepage = "https://xgitlab.cels.anl.gov/sds/ssg"
    git='https://xgitlab.cels.anl.gov/sds/ssg.git'

    version('develop', branch='master')
    version('master', branch='master')
    version('0.4.1', tag='v0.4.1')
    version('0.4.0', tag='v0.4.0')
    version('0.3.0', tag='v0.3.0')
    version('0.2', tag='v0.2')

    patch('0001-additional-error-reporting.patch', when='@0.2')
    patch('0001-Add-an-explicit-check-for-pmix-libs.patch', when='@0.4.1')
    patch('0001-Improve-deserialize-error-reporting.patch', when='@0.4.1')

    variant('mpi', default=True, description='Build with MPI support')
    variant('pmix', default=False, description='Build with PMIx support')
    variant('drc', default=False, description='Support Cray Dynamic RDMA Credentials')

    depends_on('mpi', when='+mpi')
    depends_on('pmix', when='+pmix')
    depends_on('rdma-credentials', when="+drc")

    depends_on('autoconf@2.69', type=('build'))
    depends_on('m4', type=('build'))
    depends_on('automake', type=("build"))
    depends_on('libtool', type=("build"))
    depends_on('pkg-config', type=("build"))

    depends_on('mochi-margo@0.4:')
    depends_on('mochi-margo@0.6:', when='@0.4.1:')
    depends_on('mochi-margo@develop', when='@develop')

    def configure_args(self):
        spec = self.spec
        extra_args = []

        if '+mpi' in spec:
            extra_args.extend([
                "--enable-mpi",
                "CC=%s" % spec['mpi'].mpicc
                ])
        elif '+pmix' in spec:
            extra_args.extend([
                "--enable-pmix"
                ])

        if '+drc' in spec:
            extra_args.extend([
                "--enable-drc"
            ])

        return extra_args

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
