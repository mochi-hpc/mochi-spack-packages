from spack.pkg.builtin.prrte import Prrte as BuiltinPrrte

class Prrte(BuiltinPrrte):

    def configure_args(self):
        # spack-0.14.2 prrte configure asks for libev (--with-libev) but passes
        # libevent.  we have to replicate the configure, not extend it, until
        # released version of spack has fix.
        spec = self.spec
        config_args = [
            '--enable-shared',
            '--enable-static'
        ]

        # libevent
        config_args.append(
            '--with-libevent={0}'.format(spec['libevent'].prefix))
        # hwloc
        config_args.append('--with-hwloc={0}'.format(spec['hwloc'].prefix))
        # pmix
        config_args.append('--with-pmix={0}'.format(spec['pmix'].prefix))

        return config_args
