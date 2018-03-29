from spack import *


class Ssg(AutotoolsPackage):
    """SSG is a group membership microservice based on the Mercury RPC system.
    It provides mechanisms for bootstrapping sets of Mercury processes into
    logical groups and for managing the membership of these process groups over
    time. At a high-level, each group collectively maintains a group view,
    which is just a mapping from group member identifiers to Mercury address
    information"""

    homepage = "https://xgitlab.cels.anl.gov/sds/ssg"

    version('master', git='https://xgitlab.cels.anl.gov/sds/ssg.git')

    variant('mpi', default=False, description='Build with MPI support')

    depends_on('mpi', when='+mpi')
    depends_on('margo')

    def configure_args(self):
        spec = self.spec
        extra_args = []

        if '+mpi' in spec:
            extra_args.extend([
                "--enable-mpi",
                "CC=%s" % spec['mpi'].mpicc
                ])

        return extra_args








    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
