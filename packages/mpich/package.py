from spack.pkg.builtin.mpich import Mpich

class Mpich(Mpich):
    version('3.3.2', default=True, preferred=True, sha256='4bfaf8837a54771d3e4922c84071ef80ffebddbb6971a006038d91ee7ef959b9')
    version('3.4.benvolio', branch='benvolio', git="https://github.com/roblatham00/mpich.git", submodules=True,
             preferred=False)

    variant('benvolio', default=False, description="build ROMIO with support for Benvolio i/o proxy")

    depends_on('benvolio@master', when='+benvolio')

    def configure_args(self):
        spec = self.spec
        config_args = super(Mpich, self).configure_args()

        if '+benvolio' in spec:
            config_args.append('--with-file-system=ufs+testfs+benvolio')
        return config_args
