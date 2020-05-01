from spack import *


class MochiBake(AutotoolsPackage):
    """a Mochi microservice for remote access to raw storage regions"""

    homepage = "https://xgitlab.cels.anl.gov/sds/bake"
    url      = "https://xgitlab.cels.anl.gov/sds/bake"
    git      = 'https://xgitlab.cels.anl.gov/sds/bake.git'

    version('develop', branch='master')
    version('master', branch='master')
    version('0.4.1', tag='v0.4.1')
    version('0.4', tag='v0.4')
    version('dev-file-backend', branch='carns/dev-file-backend')
    version('0.3.6', tag='v0.3.6')
    version('0.3.5', tag='v0.3.5')
    version('0.3.4', tag='v0.3.4')
    version('0.3.3', tag='v0.3.3')
    version('0.3.2', tag='v0.3.2')
    version('0.3.1', tag='v0.3.1')
    version('0.3', tag='v0.3')
    version('0.2', tag='v0.2')
    version('0.1', tag='v0.1')

    variant('benchmark', default=False, description='Enable building bake-benchmark')
    variant('remi', default=False, description="Enable support for migration with REMI")
    variant('sizecheck', default=False, description="Enable size/bound checking (may degrade performance)")
    variant('timers', default=False, description="Enable timers on stdout (use for performance tuning)")

    depends_on('autoconf@2.65:', type=("build"))
    depends_on('automake@1.13.4:', type=("build"))
    depends_on('libtool', type=("build"))
    depends_on('mochi-margo@0.4:')
    depends_on('mochi-remi@0.1:', when='@:0.3.3')
    depends_on('mochi-remi@0.2.2:', when='+remi @0.3.4:')
    # dev-file-backend version still requires remi until it is rebased
    depends_on('mochi-remi@0.2.2:', when='@dev-file-backend')
    depends_on('libuuid')
    # this spec prevents @dev-file-backend from depending on pmdk
    depends_on('pmdk', when='@0.0.0:')
    depends_on('jsoncpp@1.9.1:', when='+benchmark')
    depends_on('mpi', when='+benchmark')
    # master now depends on abt-io for file backend
    depends_on('mochi-abt-io', when='@master')

    # dependencies for develop version
    depends_on('mochi-margo@develop', when='@develop')
    depends_on('mochi-remi@develop', when='+remi @develop')
    depends_on('mochi-abt-io@develop', when='@develop')

    def configure_args(self):
        spec = self.spec
        extra_args = []

        if '+benchmark' in spec:
            extra_args.append('--enable-benchmark')
            extra_args.append('CXX=%s' % spec['mpi'].mpicxx)
            extra_args.append('CC=%s' % spec['mpi'].mpicc)
        else:
            extra_args.append('--disable-benchmark')

        if '+sizecheck' in spec:
            extra_args.append('--enable-sizecheck')
        else:
            extra_args.append('--disable-sizecheck')

        if '+timers' in spec:
            extra_args.append('--enable-timers')
        else:
            extra_args.append('--disable-timers')

        if spec.satisfies('@0.3.4:'):
            if '+remi' in spec:
                extra_args.append('--enable-remi')
            else:
                extra_args.append('--disable-remi')

        return extra_args
