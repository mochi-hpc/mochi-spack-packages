from spack import *


class MochiColza(CMakePackage):
    """Colza is a Mochi microservice designed to handle collective communications
    similar to MPI (bcast, reduce, etc.) but using RPC/RDMA through Mercury."""

    homepage = "https://xgitlab.cels.anl.gov/sds/colza"
    url = "https://xgitlab.cels.anl.gov/sds/colza"
    git='https://xgitlab.cels.anl.gov/sds/colza.git'

    version('develop', branch='master')
    version('master', branch='master', preferred=True)

    depends_on('mochi-thallium @0.8:')
    depends_on('mochi-ssg @0.4: +mpi')

    # dependencies for develop version
    depends_on('mochi-thallium @develop', when='@develop')
    depends_on('mochi-ssg @develop +mpi', when='@develop')
