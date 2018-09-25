from spack import *

class Thallium(CMakePackage):
    """Thallium is a C++14 library wrapping Margo, Mercury, and Argobots and providing an object-oriented way to use these libraries."""
    homepage = "https://xgitlab.cels.anl.gov/sds/thallium"
    url = "https://xgitlab.cels.anl.gov/sds/thallium"

    version('master', git='https://xgitlab.cels.anl.gov/sds/thallium.git')

    depends_on('margo')
    # thallium relies on std::decay_t
    conflicts('%gcc@:4.9.0');


    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON" ]
        return args
