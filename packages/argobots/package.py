

from spack.pkg.builtin.argobots import Argobots

class Argobots(Argobots):

    version('master', branch='main')
    version('1.0', sha256="36a0815f7bf99900a9c9c1eef61ef9b3b76aa2cfc4594a304f6c8c3296da8def", preferred=True)
