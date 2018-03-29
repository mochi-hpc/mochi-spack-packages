from spack import *

class Thallium(CMakePackage):
    """Thallium is a C++14 library wrapping Margo, Mercury, and Argobots and providing an object-oriented way to use these libraries."""
    homepage = "https://xgitlab.cels.anl.gov/sds/thallium"
    url = "https://xgitlab.cels.anl.gov/sds/thallium"

    version('master', git='https://xgitlab.cels.anl.gov/sds/thallium.git')
    version('provider', git='https://xgitlab.cels.anl.gov/sds/thallium.git', branch='dev-provider-id')

    depends_on('margo', when='@master')
    depends_on('margo@provider', when='@provider')
