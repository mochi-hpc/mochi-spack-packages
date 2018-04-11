from spack import *


class Bake(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://xgitlab.cels.anl.gov/sds/bake"
    url      = "https://xgitlab.cels.anl.gov/sds/bake"

    version('master', git='https://xgitlab.cels.anl.gov/sds/bake.git')

    depends_on('margo')
    depends_on('libuuid')
    depends_on('pmem')
