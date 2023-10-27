# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Mofka(CMakePackage):
    """Mofka is a Mochi-based distributed event-streaming service for HPC."""

    homepage = "https://github.com/mochi-hpc/mofka"
    git = "https://github.com/mochi-hpc/mofka.git"

    maintainers("mdorier")

    version("main", branch="main")

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
