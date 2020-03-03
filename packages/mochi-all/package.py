from spack import *


class MochiAll(PythonPackage):
    """Meta package for all Mochi components"""

    homepage = "https://xgitlab.cels.anl.gov/sds/mochi-all"
    git='https://xgitlab.cels.anl.gov/sds/mochi-all.git'

    version('master', branch='master')

    depends_on('mochi-abt-io')
    depends_on('mochi-bake')
    depends_on('mochi-ch-placement')
    depends_on('mochi-dkv')
    depends_on('mochi-kv')
    depends_on('mochi-margo')
    depends_on('mochi-mdcs')
    depends_on('mochi-poesie')
    depends_on('mochi-remi')
    depends_on('mochi-ssg')
    depends_on('mochi-thallium')
