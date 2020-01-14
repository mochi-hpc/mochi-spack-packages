from spack import *


class PyTmci(PythonPackage):
    """Python library to enable generic, C++ level access to Tensorflow memory"""

    homepage = "https://xgitlab.cels.anl.gov/sds/tmci"
    url      = "https://xgitlab.cels.anl.gov/sds/tmci.git"
    git      = "https://xgitlab.cels.anl.gov/sds/tmci.git"

    version('develop',  branch="master")

    depends_on('python@3:')
    depends_on('py-setuptools')
    depends_on('tensorflow@2.0.0:')
    depends_on('py-pybind11', type=('build'))
