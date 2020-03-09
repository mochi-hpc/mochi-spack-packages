from spack import *


class PyMochiAll(PythonPackage):
    """Meta package for all Mochi Python components"""

    homepage = "https://xgitlab.cels.anl.gov/sds/mochi-all"
    git='https://xgitlab.cels.anl.gov/sds/mochi-all.git'

    version('master', branch='master', preferred=True)
    version('develop', branch='master')

    depends_on('py-mochi-bake')
    depends_on('py-mochi-sdskv')
    depends_on('py-mochi-margo')
    depends_on('py-mochi-remi')
    depends_on('py-mochi-ssg')
    depends_on('py-mochi-tmci')

    depends_on('py-mochi-bake@develop', when='@develop')
    depends_on('py-mochi-sdskv@develop', when='@develop')
    depends_on('py-mochi-margo@develop', when='@develop')
    depends_on('py-mochi-remi@develop', when='@develop')
    depends_on('py-mochi-ssg@develop', when='@develop')
    depends_on('py-mochi-tmci@develop', when='@develop')
