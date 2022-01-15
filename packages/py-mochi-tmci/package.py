from spack import *


class PyMochiTmci(PythonPackage):
    """Python Mochi library to enable generic, C++ level access to Tensorflow memory"""

    homepage = 'https://github.com/mochi-hpc/mochi-tmci'
    url      = 'https://github.com/mochi-hpc/mochi-tmci'
    git      = 'https://github.com/mochi-hpc/mochi-tmci.git'

    version('main', branch='main', preferred=True)
    version('develop', branch='main')

    variant('theta', default=False,
            description='Option to enable when building on Theta')

    depends_on('python@3:')
    depends_on('py-tensorflow@2.0.0:', type=('build', 'link', 'run'))
    depends_on('py-pybind11', type=('build'))

    @run_before('install')
    def move_file(self):
        if '+theta' in self.spec:
            src = self.stage.source_path+'/theta/tensorflow.json'
            dst = self.stage.source_path+'/tensorflow.json'
            copy(src, dst)
