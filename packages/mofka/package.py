# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Mofka(CMakePackage):
    """Mofka is a Mochi-based distributed event-streaming service for HPC."""

    url = "https://github.com/mochi-hpc/mofka/archive/refs/tags/v0.0.1.tar.gz"
    homepage = "https://github.com/mochi-hpc/mofka"
    git = "https://github.com/mochi-hpc/mofka.git"

    maintainers("mdorier")

    version("main", branch="main")
    version("develop", branch="main")
    version("0.0.3", sha256="429beac2735c0a75cacf39d1523d26772ad9ddaa42552ba972a033f1cc8f7b35")
    version("0.0.2", sha256="024c18be993a3fe6cde6918b81486c2a9727050da060800a92a634355d8ad83d")
    version("0.0.1", sha256="ba58521053ab3c1d6ba08614257c11c7e15e51636c2fc24415fcf8cf20451365")

    variant("python", default=True, when="@0.0.3:",
            description="Enable python support")

    depends_on("pkg-config", type=("build",))
    depends_on("uuid")
    depends_on("spdlog+fmt_external")
    depends_on("fmt")
    depends_on("tclap")
    depends_on("nlohmann-json", when="@main,develop")
    depends_on("nlohmann-json-schema-validator", type=("build",), when="@main,develop")
    depends_on("rapidjson", when="@:0.0.3")
    depends_on("valijson", when="@:0.0.3")
    depends_on("mochi-thallium")
    depends_on("mochi-bedrock@0.8.3:0.9.2+ssg", when="@:0.0.2")
    depends_on("mochi-bedrock@0.10.0:+ssg", when="@0.0.3:")
    depends_on("mochi-bedrock+python", when="+python")
    depends_on("mochi-yokan@0.2.0:+bedrock", when="@0.0.2:")
    depends_on("mochi-warabi@0.4.2:+bedrock", when="@0.0.2:")

    depends_on("mochi-thallium@develop", when="@develop")
    depends_on("mochi-bedrock@develop", when="@develop")
    depends_on("mochi-yokan@develop", when="@develop")
    depends_on("mochi-warabi@develop", when="@develop")

    def cmake_args(self):
        args = ["-DENABLE_BAKE=OFF"]
        if "+python" in self.spec:
            args.append("-DENABLE_PYTHON=ON")
        return args
