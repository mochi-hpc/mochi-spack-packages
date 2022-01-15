##############################################################################
#
# Installing flamestore:
#
#     spack install flamestore
#
from spack import *


class Flamestore(PythonPackage):
    """Transient distributed object store for deep learning"""

    homepage = 'https://github.com/mochi-hpc/flamestore'
    url      = 'https://github.com/mochi-hpc/flamestore'
    git      = 'https://github.com/mochi-hpc/flamestore.git'

    version('main', branch='develop', preferred=True)
    version('develop', branch='develop')

    variant('theta', default=False,
            description='Option to enable when building on Theta')

    depends_on('jsoncpp')
    depends_on('py-spdlog')
    depends_on('spdlog')
    depends_on('py-pkgconfig')
    depends_on('py-pybind11')

    # normal versions
    depends_on('py-mochi-bake@master')
    depends_on('mochi-ssg@0.4:')
    depends_on('mochi-sdskv')
    depends_on('mochi-thallium@0.5.3:')
    depends_on('py-mochi-margo')
    depends_on('py-mochi-tmci')

    # develop version
    depends_on('py-mochi-bake@develop', when='@develop')
    depends_on('mochi-ssg@develop', when='@develop')
    depends_on('mochi-sdskv@develop', when='@develop')
    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('py-mochi-margo@develop', when='@develop')
    depends_on('py-mochi-tmci@develop', when='@develop')

    @run_before('install')
    def move_file(self):
        if '+theta' in self.spec:
            src = self.stage.source_path+'/theta/tensorflow.json'
            dst = self.stage.source_path+'/tensorflow.json'
            copy(src, dst)
