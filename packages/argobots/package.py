

from spack.pkg.builtin.argobots import Argobots

class Argobots(Argobots):

    # these are available upstream, but we also define them here for users
    # working against previous spack releases
    version("1.1", sha256="f0f971196fc8354881681c2282a2f2adb6d48ff5e84cf820ca657daad1549005")
    version("1.0.1", sha256="fa05a02d7f8f74d845647636609219ee02f6adf628ebcbf40393f829987d9036")
    version("1.0", sha256="36a0815f7bf99900a9c9c1eef61ef9b3b76aa2cfc4594a304f6c8c3296da8def")

    variant('stack-unwind', default=False, description='Enable stack unwinding')
    conflicts('+stack-unwind', when='@:1.0.1',
              msg='+stack-unwind variant only available for @1.1 or newer')
    depends_on("libunwind", when="+stack-unwind")

    def configure_args(self):
        spec = self.spec
        config_args = super(Argobots, self).configure_args()

        if '+stack-unwind' in spec:
            config_args.append('--enable-stack-unwind')
        else:
            config_args.append('--disable-stack-unwind')

        return config_args
