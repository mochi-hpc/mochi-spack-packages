from spack import *


class PyMochiAll(CMakePackage):
    """Meta package for all Mochi Python components"""

    homepage = "https://xgitlab.cels.anl.gov/sds/mochi-all"
    git='https://xgitlab.cels.anl.gov/sds/mochi-all.git'

    version('master', branch='master', preferred=True)
    version('develop', branch='master')

    variant('bake', default=True, description='Build py-mochi-bake')
    variant('sdskv', default=True, description='Build py-mochi-sdskv')
    variant('margo', default=True, description='Build py-mochi-margo')
    variant('remi', default=True, description='Build py-mochi-remi')
    variant('ssg', default=True, description='Build py-mochi-ssg')
    variant('tmic', default=False, description='Build py-mochi-tmic')

    depends_on('py-mochi-bake', when='+bake')
    depends_on('py-mochi-sdskv', when='+sdskv')
    depends_on('py-mochi-margo', when='+margo')
    depends_on('py-mochi-remi', when='+remi')
    depends_on('py-mochi-ssg', when='+ssg')
    depends_on('py-mochi-tmci', when='+tmic')

    depends_on('py-mochi-bake@develop', when='+bake @develop')
    depends_on('py-mochi-sdskv@develop', when='+sdskv @develop')
    depends_on('py-mochi-margo@develop', when='+margo @develop')
    depends_on('py-mochi-remi@develop', when='+remi @develop')
    depends_on('py-mochi-ssg@develop', when='+ssg @develop')
    depends_on('py-mochi-tmci@develop', when='+tmci @develop')
