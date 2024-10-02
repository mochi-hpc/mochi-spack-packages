from spack.package import *
from spack import *
import llnl.util.tty as tty


class MochiBedrockModuleApi(CMakePackage):
    """Module API for Mochi's Bedrock component"""

    homepage = "https://github.com/mochi-hpc/mochi-bedrock-module-api"
    url = "https://github.com/mochi-hpc/mochi-bedrock-module-api/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/mochi-hpc/mochi-bedrock-module-api.git"

    version("main", branch="main")
    version("develop", branch="main")
    version("0.2.0", sha256="94c56d64c77932ec06a6ea74beba182dac08eb25a79d7ffe9a51b29adaf3d614")
    version("0.1.0", sha256="44b2622f90a39b23fab59d4ffa15721ff59138fe0f1ceca9491efd9324489a9d")

    provides("mochi-bedrock-headers")

    depends_on("mochi-thallium@0.12.0:")

    depends_on("mochi-thallium@develop", when="@develop")

    depends_on("cmake@3.8:", type="build")
    depends_on("nlohmann-json")
    depends_on("spdlog")
    depends_on("tclap")
    depends_on("fmt", when="@0.4.1:")
