

from spack.pkg.builtin.argobots import Argobots as BuiltinArgobots

class Argobots(BuiltinArgobots):

    # these are available upstream, but we also define them here for users
    # working against previous spack releases
    version("1.1", sha256="f0f971196fc8354881681c2282a2f2adb6d48ff5e84cf820ca657daad1549005")
    version("1.0.1", sha256="fa05a02d7f8f74d845647636609219ee02f6adf628ebcbf40393f829987d9036")
    version("1.0", sha256="36a0815f7bf99900a9c9c1eef61ef9b3b76aa2cfc4594a304f6c8c3296da8def")

    # some of these may be duplicated upstream; we want to cover them so
    # that they are available when using the mochi spack repo

    variant("perf", default=True, description="Add performance optimization flags")
    variant("valgrind", default=False, description="Enable Valgrind")
    variant("debug", default=False, description="Compiled with debugging symbols")
    variant("stackunwind", default=False, description="Enable function stack unwinding")
    variant("stackguard", default="none", description="Enable stack guard",
            values=('none', 'canary-32', 'mprotect', 'mprotect-strict'), multi=False)
    variant("tool", default=False, description="Enable ABT_tool interface")
    variant("affinity", default=False, description="Enable affinity setting")

    depends_on("valgrind", when="+valgrind")
    depends_on("libunwind", when="+stackunwind")

    def configure_args(self):
        spec = self.spec
        args = super(Argobots, self).configure_args()

        if '+perf' in self.spec:
            args.append('--enable-perf-opt')

        if '+valgrind' in self.spec:
            args.append('--enable-valgrind')
        else:
            args.append('--disable-valgrind')

        if '+debug' in self.spec:
            args.append('--enable-debug=yes')
        else:
            args.append('--disable-debug')

        if '+stackunwind' in self.spec:
            args.append('--enable-stack-unwind')
            args.append('--with-libunwind={0}'.format(self.spec['libunwind'].prefix))

        stackguard = self.spec.variants['stackguard'].value
        if stackguard != 'none':
            args.append('--enable-stack-overflow-check={0}'.format(stackguard))

        if '+tool' in self.spec:
            args.append('--enable-tool')

        if '+affinity' in self.spec:
            args.append('--enable-affinity')

        return args
