from spack import *


class MochiAll(PythonPackage):
    """Meta package for all Mochi components"""

    homepage = "https://xgitlab.cels.anl.gov/sds/mochi-all"
    git='https://xgitlab.cels.anl.gov/sds/mochi-all.git'

    version('master', branch='master', preferred=True)
    version('develop', branch='master')

    depends_on('mochi-abt-io')
    depends_on('mochi-bake')
    depends_on('mochi-ch-placement')
    depends_on('mochi-dkv')
    depends_on('mochi-sdskv')
    depends_on('mochi-margo')
    depends_on('mochi-mdcs')
    depends_on('mochi-poesie')
    depends_on('mochi-remi')
    depends_on('mochi-ssg')
    depends_on('mochi-thallium')

    depends_on('mochi-abt-io@develop', when='@develop')
    depends_on('mochi-bake@develop', when='@develop')
    depends_on('mochi-ch-placement@develop', when='@develop')
    depends_on('mochi-dkv@develop', when='@develop')
    depends_on('mochi-sdskv@develop', when='@develop')
    depends_on('mochi-margo@develop', when='@develop')
    depends_on('mochi-mdcs@develop', when='@develop')
    depends_on('mochi-poesie@develop', when='@develop')
    depends_on('mochi-remi@develop', when='@develop')
    depends_on('mochi-ssg@develop', when='@develop')
    depends_on('mochi-thallium@develop', when='@develop')
