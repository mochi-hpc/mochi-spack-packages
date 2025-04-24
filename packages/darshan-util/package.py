from spack.package import *
from spack.pkg.builtin.darshan_util import DarshanUtil as BuiltinDarshanUtil


class DarshanUtil(BuiltinDarshanUtil):
    version('dask', branch='snyder/dxt-extra-info-pthread-id', git="https://github.com/darshan-hpc/darshan.git", submodules=True)
    
    depends_on("autoconf", type="build", when="@dask")
    depends_on("automake", type="build", when="@dask")
    depends_on("libtool", type="build", when="@dask")
    depends_on("m4", type="build", when="@dask")
