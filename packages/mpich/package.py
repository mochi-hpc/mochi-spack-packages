from spack.pkg.builtin.mpich import Mpich as BuiltinMpich

class Mpich(BuiltinMpich):
    version('3.4.2', sha256='5c19bea8b84e8d74cca5f047e82b147ff3fba096144270e3911ad623d6c587bf')
    version('3.4.1', sha256='8836939804ef6d492bcee7d54abafd6477d2beca247157d92688654d13779727')
    version('3.4',   sha256='ce5e238f0c3c13ab94a64936060cff9964225e3af99df1ea11b130f20036c24b')
    version('3.3.2', sha256='4bfaf8837a54771d3e4922c84071ef80ffebddbb6971a006038d91ee7ef959b9')
    version('3.4.benvolio', branch='benvolio', git="https://github.com/roblatham00/mpich.git", submodules=True,
             preferred=False)

    variant('benvolio', default=False, description="build ROMIO with support for Benvolio i/o proxy")
    variant('argobots', default=False, description="enable Argobots support")

    depends_on('benvolio@master', when='+benvolio')
    depends_on('argobots', when='+argobots')

    def configure_args(self):
        spec = self.spec
        config_args = super(Mpich, self).configure_args()

        if '+benvolio' in spec:
            config_args.append('--with-file-system=ufs+testfs+benvolio')

        if '+argobots' in spec:
            config_args.append('--with-thread-package=argobots')
            config_args.append('--with-argobots=' + spec['argobots'].prefix)

        return config_args
