from spack import *


class BakeBulk(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://xgitlab.cels.anl.gov/sds/bake-bulk"
    url      = "https://xgitlab.cels.anl.gov/sds/bake-bulk"

    version('master', git='git@xgitlab.cels.anl.gov:sds/bake-bulk.git')

    depends_on('margo')
    depends_on('libuuid')
    depends_on('pmem')
#    depends_on('pandoc', type=("build") );
