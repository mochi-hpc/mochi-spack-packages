# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install mochi-warabi
#
# You can edit this file again by typing:
#
#     spack edit mochi-warabi
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class MochiWarabi(CMakePackage):
    """Warabi is a BLOB-storage microservice for Mochi."""

    homepage = "https://github.com:/mochi-hpc/mochi-warabi"
    git = "https://github.com:/mochi-hpc/mochi-warabi.git"

    maintainers("mdorier")

    version("main", branch="main", preferred=True)
    version("develop", branch="main")

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
