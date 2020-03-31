from spack import *

class MochiSonata(CMakePackage):
    """Sonata is a Mochi-based document store that uses UnQLite as a backend."""

    homepage = "https://xgitlab.cels.anl.gov/sds/sonata"
    url = "https://xgitlab.cels.anl.gov/sds/sonata"
    git = "https://xgitlab.cels.anl.gov/sds/sonata.git"

    version('master', branch='master', preferred=True)
    version('develop', branch='master')
    version('0.1', tag='v0.1')

    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('mochi-thallium')
    depends_on('unqlite')
    depends_on('tclap', type=('build', 'link'))
    depends_on('jsoncpp')
    depends_on('spdlog')
    depends_on('cmake', type=('build'))

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON" ]
        return args
