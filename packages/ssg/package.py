from spack import *


class Ssg(AutotoolsPackage):
    """SSG is a group membership microservice based on the Mercury RPC system.
    It provides mechanisms for bootstrapping sets of Mercury processes into
    logical groups and for managing the membership of these process groups over
    time. At a high-level, each group collectively maintains a group view,
    which is just a mapping from group member identifiers to Mercury address
    information"""

    homepage = "https://xgitlab.cels.anl.gov/sds/ssg"
    git='https://xgitlab.cels.anl.gov/sds/ssg.git'

    version('develop', branch='master')
    version('0.3.0', tag='v0.3.0')
    version('0.2', tag='v0.2')

    patch('0001-additional-error-reporting.patch', when='@0.2')

    variant('mpi', default=True, description='Build with MPI support')
    variant('pmix', default=False, description='Build with PMIx support')

    depends_on('mpi', when='+mpi')
    depends_on('pmix', when='+pmix')
    depends_on('margo@0.4:')
    depends_on('autoconf@2.69', type='build')

    def configure_args(self):
        spec = self.spec
        extra_args = []

        if '+mpi' in spec:
            extra_args.extend([
                "--enable-mpi",
                "CC=%s" % spec['mpi'].mpicc
                ])
        else if '+pmix' in spec:
            extra_args.extend([
                "--enable-pmix"
                ])


        return extra_args








    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
