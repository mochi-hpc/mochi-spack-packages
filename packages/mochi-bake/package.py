from spack import *


class MochiBake(AutotoolsPackage):
    """a Mochi microservice for remote access to raw storage regions"""

    homepage = 'https://github.com/mochi-hpc/mochi-bake/'
    url      = 'https://github.com/mochi-hpc/mochi-bake/archive/v0.6.tar.gz'
    git      = 'https://github.com/mochi-hpc/mochi-bake.git'

    version('develop', branch='main')
    version('main', branch='main')
    version('0.6.3', sha256='e53bdab06bf38548e47430c435e4ea47f27f30d4866c9e6e5da1c227d32fd92e')
    version('0.6.2', sha256='0ecefab1ce25f2c4450080255f0adafe1ee8ce3496507e422f800fc648d61ffc')
    version('0.6.1', sha256='178a8bed163910df9dcd20b94508f94387db7814d0af45db8cf57fc2d9a432ce')
    version('0.6',   sha256='9328bf07f534ad992afde23eac90404416c88f30c5c818969aecae98bee3479f')
    version('0.5.0', sha256='b839f6aefe35645af6e870690a9be7081faf5b3c9624db6b8e4f444e0510d0be')
    version('0.4.1', sha256='e61d1e48cd5bd3e93960dfa4b4c344200fa06c815942875e63a90ae1e872fede')
    version('0.4',   sha256='a08b0ad41f900d5236699e2d27708737ee7c7ad76f65f661b514fc8c4210a315')
    version('0.3.6', sha256='8e5a60cc17ca9061a1bd7c21dc8d96ceca56ee85b1ccc98227f921dd49ce60d9')
    version('0.3.5', sha256='a8790611a26bd33bb76dc95d09c0c94cbe43c6441b779575abcaca47380afa9a')
    version('0.3.4', sha256='754ef4e5747856f177c9becceb7036a692bfeb0e216813fe5134d7419fec2431')
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
    variant('bedrock', default=True, description='Enable building Bedrock module')

    depends_on('autoconf@2.65:', type=("build"))
    depends_on('automake@1.13.4:', type=("build"))
    depends_on('libtool', type=("build"))
    depends_on('pmdk')
    depends_on('uuid')
    depends_on('jsoncpp@1.9.1:', when='+benchmark')
    depends_on('mpi', when='+benchmark')

    # dependencies for normal versions
    depends_on('mochi-margo@0.4:')
    depends_on('mochi-abt-io')
    depends_on('mochi-bedrock', when='+bedrock')
    depends_on('mochi-remi@0.1:', when='@:0.3.3')
    depends_on('mochi-remi@0.2.2:', when='+remi @0.3.4:')

    # dependencies for develop version
    depends_on('mochi-margo@develop', when='@develop')
    depends_on('mochi-remi@develop', when='+remi @develop')
    depends_on('mochi-abt-io@develop', when='@develop')
    depends_on('mochi-bedrock@develop', when='@develop +bedrock')

    conflicts('+bedrock', when='@:0.5',
              msg='+bedrock variant only available starting from 0.6')

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

        if '+bedrock' in spec:
            extra_args.append('--enable-bedrock')
        else:
            extra_args.append('--disable-bedrock')

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
