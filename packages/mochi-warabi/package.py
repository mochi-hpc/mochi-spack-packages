# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class MochiWarabi(CMakePackage):
    """Warabi is a BLOB-storage microservice for Mochi."""

    url = "https://github.com/mochi-hpc/mochi-warabi/archive/refs/tags/v0.1.0.tar.gz"
    homepage = "https://github.com:/mochi-hpc/mochi-warabi"
    git = "https://github.com:/mochi-hpc/mochi-warabi.git"

    maintainers("mdorier")

    version("main", branch="main")
    version("develop", branch="main")
    version("0.2.0", sha256="35ad6cc45ac1e28fc3d68984acedab692bebd2979bb05b0d29a8001f5819c34b")
    version("0.1.0", sha256="a327f1a0c63e5e913b1d16e9cd73590e9f7b675acd187d9938cb3dcc5210486f")

    variant("bedrock", default=False, description="Enable Bedrock support")
    variant("remi", default=False, description="Enable REMI support")

    depends_on("pkgconfig")
    depends_on("uuid")
    depends_on("nlohmann-json")
    depends_on("pmdk")
    depends_on("spdlog")
    depends_on("fmt")
    depends_on("tclap")
    depends_on("valijson")

    depends_on("mochi-thallium@0.11.3:")
    depends_on("mochi-bedrock", when="+bedrock")
    depends_on("mochi-abt-io")
    depends_on("mochi-remi", when="+remi")

    depends_on("mochi-thallium@0.12.0:", when="@0.2.0:")
    depends_on("mochi-margo@0.15.0:", when="@0.2.0:")
    depends_on("mochi-remi@0.4.0:", when="+remi @0.2.0:")
    depends_on("mochi-bedrock@0.8.0:", when="+bedrock @0.2.0:")

    depends_on("mochi-thallium@develop", when="@develop")
    depends_on("mochi-bedrock@develop", when="@develop +bedrock")
    depends_on("mochi-abt-io@develop", when="@develop")
    depends_on("mochi-remi@develop", when="@develop +remi")

    def cmake_args(self):
        args = []
        variant_bool = lambda feature: str(feature in self.spec)
        args.append("-DENABLE_BEDROCK:BOOL=%s" % variant_bool("+bedrock"))
        args.append("-DENABLE_REMI:BOOL=%s" % variant_bool("+remi"))
        return args
