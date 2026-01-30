from spack.package import *
from spack import *


class MochiBedrockModuleApi(CMakePackage):
    """Module API for Mochi's Bedrock component"""

    homepage = "https://github.com/mochi-hpc/mochi-bedrock-module-api"
    url = "https://github.com/mochi-hpc/mochi-bedrock-module-api/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/mochi-hpc/mochi-bedrock-module-api.git"

    version("main", branch="main")
    version("develop", branch="main")
    version("0.2.1", sha256="cfcec755a27eaf2c6732d1cb031d04919f6de1f4d0fe4d09f6ed72c25c008146")
    version("0.2.0", sha256="94c56d64c77932ec06a6ea74beba182dac08eb25a79d7ffe9a51b29adaf3d614")
    version("0.1.0", sha256="44b2622f90a39b23fab59d4ffa15721ff59138fe0f1ceca9491efd9324489a9d")

    provides("mochi-bedrock-headers")

    depends_on("mochi-thallium@0.12.0:")

    depends_on("mochi-thallium@develop", when="@develop")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.8:", type="build")
    depends_on("nlohmann-json")
    depends_on("spdlog")
    depends_on("fmt")
