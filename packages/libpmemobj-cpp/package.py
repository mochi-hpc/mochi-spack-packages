from spack import *


class LibpmemobjCpp(CMakePackage):
    """C++ bindings for libpmemobj (https://github.com/pmem/pmdk)"""

    homepage = "https://github.com/pmem/libpmemobj-cpp"
    url      = "https://github.com/pmem/libpmemobj-cpp"
    git      =  "https://github.com/pmem/libpmemobj-cpp.git"

    version('master', git='https://github.com/pmem/libpmemobj-cpp.git')
    version('1.5', tag='1.5')
    version('1.5.1', tag='1.5.1')

    # libpmemobj seems to only understand 'Debug' and 'Release'
    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release'))


    depends_on('pmdk@1.4:')

    def cmake_args(self):
        # Add arguments other than
        # CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        args = []
        return args
