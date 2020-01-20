##############################################################################
#
# Installing flamestore:
#
#     spack install flamestore
#
from spack import *


class Flamestore(PythonPackage):
    """Transient distributed object store for deep learning"""

    homepage = "https://xgitlab.cels.anl.gov/sds/flamestore"
    url      = "https://xgitlab.cels.anl.gov/sds/flamestore"
    git      = "https://xgitlab.cels.anl.gov/sds/flamestore.git"

    version('develop', branch='dev-refactoring')
   
    variant('theta', default=False,
            description='Option to enable when building on Theta')

    depends_on('margo@0.6:')
    depends_on('py-bake')
    depends_on('ssg@0.4:')
    depends_on('sdskeyval')
    depends_on('py-margo@0.3:')
    depends_on('thallium@0.5:')
    depends_on('jsoncpp')
    depends_on('py-spdlog')
    depends_on('spdlog')
    depends_on('py-pkgconfig')
    depends_on('py-pybind11')
    depends_on('py-tmci')

    @run_before('build')
    def move_file(self):
        if '+theta' in self.spec:
            src = self.stage.source_path+'/theta/tensorflow.json'
            dst = self.stage.source_path+'/tensorflow.json'
            copy(src, dst)
