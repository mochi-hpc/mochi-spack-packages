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
    version("0.0.1", sha256="ba58521053ab3c1d6ba08614257c11c7e15e51636c2fc24415fcf8cf20451365")

    depends_on("pkg-config", type=("build",))
    depends_on("uuid")
    depends_on("rapidjson")
    depends_on("valijson")
    depends_on("spdlog+fmt_external")
    depends_on("fmt")
    depends_on("tclap")
    depends_on("mochi-thallium")
    depends_on("mochi-bedrock@0.6.0:+ssg")

    def cmake_args(self):
        args = ["-DENABLE_BAKE=OFF"]
        return args
