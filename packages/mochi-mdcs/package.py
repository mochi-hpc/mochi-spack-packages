from spack import *

class MochiMdcs(CMakePackage):
    """MDCS is Mochi's Diagnostic Counters Service, a service that exposes a set of
    counters in a server to be accessible by remote clients for monitoring the server."""

    homepage = "https://xgitlab.cels.anl.gov/sds/mdcs"
    url = "https://xgitlab.cels.anl.gov/sds/mdcs"
    git='https://xgitlab.cels.anl.gov/sds/mdcs.git'

    version('master', branch='master', preferred=True)
    version('develop', branch='master')

    depends_on('mochi-margo')
    depends_on('mochi-margo@develop', when='@develop')
