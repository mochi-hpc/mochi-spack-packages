from spack.package import *
from spack import *
import llnl.util.tty as tty


class MochiBedrockModuleApi(CMakePackage):
    """Module API for Mochi's Bedrock component"""

    homepage = "https://github.com/mochi-hpc/mochi-bedrock-module-api"
    url = "https://github.com/mochi-hpc/mochi-bedrock-module-api/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/mochi-hpc/mochi-bedrock-module-api.git"

    version("develop", branch="main")
    version("main", branch="main", preferred=True)

    depends_on("mochi-thallium@0.12.0:")

    depends_on("mochi-thallium@develop", when="@develop")

    depends_on("cmake@3.8:", type="build")
    depends_on("nlohmann-json")
    depends_on("spdlog")
    depends_on("tclap")
    depends_on("fmt", when="@0.4.1:")
