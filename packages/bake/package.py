from spack import *


class Bake(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://xgitlab.cels.anl.gov/sds/bake"
    url      = "https://xgitlab.cels.anl.gov/sds/bake"

    version('master', git='git@xgitlab.cels.anl.gov:sds/bake.git')
    version('provider', git='git@xgitlab.cels.anl.gov:sds/bake.git', branch='dev-provider-id')

    depends_on('margo', when='@master')
    depends_on('margo@provider', when='@provider')
    depends_on('libuuid')
    depends_on('pmem')
#    depends_on('pandoc', type=("build") );
