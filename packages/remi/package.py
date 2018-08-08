from spack import *


class Remi(CMakePackage):
    """REMI is a Mochi microservice designed to handle the migration of sets of files
    from a node to another. It uses RDMA and memory mapping to efficiently transfer
    potentially large groups of files at once."""

    homepage = "https://xgitlab.cels.anl.gov/sds/remi"
    url = "https://xgitlab.cels.anl.gov/sds/remi"

    version('master', git='https://xgitlab.cels.anl.gov/sds/remi.git')

    depends_on('thallium')
