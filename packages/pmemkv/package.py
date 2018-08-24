from spack import *


class Pmemkv(CMakePackage):
    """Key/Value Datastore for Persistent Memory"""


    homepage = "https://github.com/pmem/pmemkv"
    url      = "https://github.com/pmem/pmemkv.git"

    version('master', git='https://github.com/pmem/pmemkv.git')

    depends_on('libpmemobj-cpp')
    patch('0001-hack-make-install-for-spack.patch')

    def cmake_args(self):
        # Add arguments other than
        # CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        args = []
        return args

    def install(self, spec, prefix):
        make("install", "prefix=%s" % prefix)
