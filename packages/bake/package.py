from spack import *


class Bake(AutotoolsPackage):
    """Margo-enabled wrapper for Pmem, enabling RDMA to Pmem targets."""

    homepage = "https://xgitlab.cels.anl.gov/sds/bake"
    url      = "https://xgitlab.cels.anl.gov/sds/bake"
    git      = 'https://xgitlab.cels.anl.gov/sds/bake.git'

    version('develop', branch='master')
    version('dev-file-backend', branch='carns/dev-file-backend')
    version('0.3.2', tag='v0.3.2')
    version('0.3.1', tag='v0.3.1')
    version('0.3', tag='v0.3')
    version('0.2', tag='v0.2')
    version('0.1', tag='v0.1')

    variant('sizecheck', default=False, description="Enable size/bound checking (may degrade performance)")
    variant('timers', default=False, description="Enable timers on stdout (use for performance tuning)")

    depends_on('autoconf@2.65:', type=("build"))
    depends_on('automake@1.13.4:', type=("build"))
    depends_on('libtool', type=("build"))
    depends_on('margo@0.4:')
    depends_on('remi@0.1:')
    depends_on('libuuid')
    depends_on('pmdk')

    def configure_args(self):
        spec = self.spec
        extra_args = []

        if '+sizecheck' in spec:
            extra_args.append('--enable-sizecheck')
        else:
            extra_args.append('--disable-sizecheck')

        if '+timers' in spec:
            extra_args.append('--enable-timers')
        else:
            extra_args.append('--disable-timers')

        return extra_args
