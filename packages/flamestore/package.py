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
    
    depends_on('margo@0.6:')
    depends_on('bake')
    depends_on('ssg@0.4:')
    depends_on('sdskeyval')
    depends_on('py-margo@0.3:')
    depends_on('thallium@0.5:')
    depends_on('jsoncpp')
    depends_on('py-spdlog')
    depends_on('spdlog')
    depends_on('py-pkgconfig')
    depends_on('py-pybind11')
