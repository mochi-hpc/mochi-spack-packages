from spack import *


class Remi(CMakePackage):
    """REMI is a Mochi microservice designed to handle the migration of sets of files
    from a node to another. It uses RDMA and memory mapping to efficiently transfer
    potentially large groups of files at once."""

    homepage = "https://xgitlab.cels.anl.gov/sds/remi"
    url = "https://xgitlab.cels.anl.gov/sds/remi"
    git='https://xgitlab.cels.anl.gov/sds/remi.git'

    version('develop', branch='master')
    version('0.1', tag='v0.1')

    depends_on('thallium@0.3:')
    depends_on('libuuid')
    depends_on('abt-io@0.1:')

    patch('0001-explicitly-request-C-14.patch')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON" ]
        return args
