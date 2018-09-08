from spack import *


class LibpmemobjCpp(CMakePackage):
    """C++ bindings for libpmemobj (https://github.com/pmem/pmdk)"""

    homepage = "https://github.com/pmem/libpmemobj-cpp"
    url      = "https://github.com/pmem/libpmemobj-cpp.git"

    version('master', git='https://github.com/pmem/libpmemobj-cpp.git')


    depends_on('pmem@1.4')

    def cmake_args(self):
        # Add arguments other than
        # CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        args = []
        return args
