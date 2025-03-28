from spack.package import *
from spack import *


class MochiRemi(CMakePackage):
    """REMI is a Mochi microservice designed to handle the migration of sets of files
    from a node to another. It uses RDMA and memory mapping to efficiently transfer
    potentially large groups of files at once."""

    homepage = 'https://github.com/mochi-hpc/mochi-remi'
    url = 'https://github.com/mochi-hpc/mochi-remi/archive/refs/tags/v0.3.2.tar.gz'
    git = 'https://github.com/mochi-hpc/mochi-remi.git'

    version('develop', branch='main')
    version('main', branch='main')
    version("0.5.0", sha256="773c375159b493e5377fd85352f2e9b9138366729bd2fef42cf8e7e31898daa0")
    version("0.4.0", sha256="570a16711d26059c4ee60e6cbee9aaf8d3313162469c06ab2b910f40a38dd61b")
    version("0.3.3", sha256="ad481e282ed2d349a0f19cb082183614426c165ff75b2b9893543991e22fdf59")
    version("0.3.2", sha256="b289c5612316d6e65173004f0ad79e6e9123391ad79c6ac43b9a0b59dd0cf2bf")
    version('0.3.1', tag='v0.3.1')
    version('0.3', tag='v0.3')
    version('0.2.3', tag='v0.2.3')
    version('0.2.2', tag='v0.2.2')
    version('0.2.1', tag='v0.2.1')
    version('0.2', tag='v0.2')
    version('0.1.1', tag='v0.1.1')
    version('0.1', tag='v0.1')

    variant('bedrock', default=True, description='Enable building Bedrock module')

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on('cmake@3.12:', type='build')
    depends_on('mochi-thallium@0.12.0:', when='@0.4.0:')
    depends_on('mochi-thallium@0.6.0:', when='@0.2.3:')
    depends_on('mochi-thallium@0.4.2:', when='@0.2.2')
    depends_on('mochi-thallium@0.3:', when='@:0.2.1')
    depends_on('mochi-abt-io@0.1:')
    depends_on('mochi-bedrock@0.2:0.14.2', when='@0.3:0.4.0 +bedrock')
    depends_on('mochi-bedrock-module-api@0.2.0:', when='@0.5.0: +bedrock')
    depends_on('uuid')

    # dependencies for develop version
    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('mochi-abt-io@develop', when='@develop')
    depends_on('mochi-bedrock@develop', when='@develop +bedrock')

    patch('0001-explicitly-request-C-14.patch')

    conflicts('+bedrock', when='@:0.2.3',
              msg='+bedrock variant only available starting from 0.3')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON" ]
        if '+bedrock' in self.spec:
            args.append('-DENABLE_BEDROCK=ON')
        else:
            args.append('-DENABLE_BEDROCK=OFF')
        return args
