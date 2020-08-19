from spack import *


class MochiColza(CMakePackage):
    """Colza is a Mochi microservice designed to handle collective communications
    similar to MPI (bcast, reduce, etc.) but using RPC/RDMA through Mercury."""

    homepage = "https://xgitlab.cels.anl.gov/sds/colza"
    url = "https://xgitlab.cels.anl.gov/sds/colza"
    git='https://xgitlab.cels.anl.gov/sds/colza.git'

    version('develop', branch='master')
    version('master', branch='master', preferred=True)
    version('no-rma', branch='dev-better-p2p')

    depends_on('libuuid')
    depends_on('mochi-thallium @0.8:')

    # dependencies for develop version
    depends_on('mochi-thallium @develop', when='@develop')
    depends_on('mpi')
