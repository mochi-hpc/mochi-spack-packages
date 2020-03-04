from spack import *


class PyMochiAll(PythonPackage):
    """Meta package for all Mochi Python components"""

    homepage = "https://xgitlab.cels.anl.gov/sds/mochi-all"
    git='https://xgitlab.cels.anl.gov/sds/mochi-all.git'

    version('master', branch='master')

    depends_on('py-mochi-bake')
    depends_on('py-mochi-sdskv')
    depends_on('py-mochi-margo')
    depends_on('py-mochi-remi')
    depends_on('py-mochi-ssg')
    depends_on('py-mochi-tmci')
