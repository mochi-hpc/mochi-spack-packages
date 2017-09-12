from spack import *

class Mdcs(CMakePackage):
    """MDCS is Mochi's Diagnostic Counters Service, a service that exposes a set of counters in a server to be accessible by remote clients for monitoring the server."""
    homepage = "https://xgitlab.cels.anl.gov/sds/mdcs"
    url = "https://xgitlab.cels.anl.gov/sds/mdcs"

    version('develop', git='https://xgitlab.cels.anl.gov/sds/mdcs.git')

    depends_on('boost')
    depends_on('mercury')
    depends_on('argobots')
    depends_on('margo@margo-registered-data')
