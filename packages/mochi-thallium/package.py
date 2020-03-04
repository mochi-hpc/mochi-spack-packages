from spack import *

class MochiThallium(CMakePackage):
    """A Mochi C++14 library wrapping Margo, Mercury,
    and Argobots and providing an object-oriented way to use these libraries."""

    homepage = "https://xgitlab.cels.anl.gov/sds/thallium"
    url = "https://xgitlab.cels.anl.gov/sds/thallium"
    git = "https://xgitlab.cels.anl.gov/sds/thallium.git"

    version('develop', branch='master')
    version('0.5.2', tag='v0.5.2')
    version('0.5.1', tag='v0.5.1')
    version('0.5', tag='v0.5')
    version('0.4.2', tag='v0.4.2')
    version('0.4.1', tag='v0.4.1')
    version('0.4', tag='v0.4')
    version('0.3.4', tag='v0.3.4')
    version('0.3.3', tag='v0.3.3')
    version('0.3.2', tag='v0.3.2')
    version('0.3.1', tag='v0.3.1')
    version('0.3', tag='v0.3')

    variant('cereal', default=False,
            description='Use the cereal library for serialization')

    depends_on('mochi-margo@develop', when='@develop')
    depends_on('mochi-margo@0.6:', when='@0.5:')
    depends_on('mochi-margo@0.4:', when='@:0.3.4')
    depends_on('mochi-margo@0.5:', when='@0.4:0.4.2')
    depends_on('cereal', when='@0.4.1: +cereal')
    # thallium relies on std::decay_t
    conflicts('%gcc@:4.9.0');

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON" ]
        return args
