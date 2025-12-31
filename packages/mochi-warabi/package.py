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
    version("0.7.0", sha256="a4c696bc1e06d2959d5d2e3673de850bec38c3058981a43205a97e963bca2b1f")
    version("0.6.3", sha256="8e1fbea5ff84271a83f353902e28dab7095daae4a7a94ff621432f6c19283799")
    version("0.6.2", sha256="5d654704a5d96d2c56d69ddaa2fd1edc267b692f590282ddcb107cca14630a93")
    version("0.6.1", sha256="27e4f5bbb31fbd18985beea64a95b25f14f0a3a65f29f49d6d8472ad768f56e3")
    version("0.6.0", sha256="99e4f16cf924304ff957a613bb87e22f1a3f99945fee51cb6e7bf15d13c1a232")
    version("0.5.0", sha256="2455f9dffe6c9880a27468ad185ddbc2fbe9b3b037d94c06d8113088a1acc45d")
    version("0.4.0", sha256="ec532f045675d3061dd41a0cac49dbaa0c6e2ea3450b6938979cfaa5710bbf73")
    version("0.3.0", sha256="476009ca8abfa1256e7ddfb6ea1d1509b1d230109c34f4cc24d531ca581849e3")
    version("0.2.0", sha256="35ad6cc45ac1e28fc3d68984acedab692bebd2979bb05b0d29a8001f5819c34b")
    version("0.1.0", sha256="a327f1a0c63e5e913b1d16e9cd73590e9f7b675acd187d9938cb3dcc5210486f")

    variant("python", default=False, description="Enable Python support")
    variant("bedrock", default=True, description="Enable Bedrock support")
    variant("remi", default=False, description="Enable REMI support", when="@0.5.0:")
    variant("space", default=False, description="Enable configuration space", when="@0.5.0:")

    conflicts("~python", when="+space")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("pkgconfig", type=("build",))
    depends_on("uuid")
    depends_on("nlohmann-json")
    depends_on("nlohmann-json-schema-validator@2.3.0:", when="@0.3.0:")
    depends_on("pmdk")
    depends_on("spdlog")
    depends_on("fmt")
    depends_on("tclap", type=("build",))
    depends_on("valijson", when="@:0.2.0")
    depends_on("py-pybind11", then="@0.7.0: +python")

    depends_on("mochi-thallium@0.11.3:")
    depends_on("mochi-bedrock@:0.14.2", when="+bedrock @:0.3.0")
    depends_on("mochi-bedrock-module-api@0.2.0:", when="+bedrock @0.6.0:")
    depends_on("mochi-bedrock-module-api@0.1.0", when="+bedrock @0.4.0:0.5.0")
    depends_on("mochi-abt-io")
    depends_on("mochi-abt-io@0.8.0:", when="@0.6.0:")
    depends_on("mochi-remi", when="+remi")
    depends_on("py-mochi-margo@0.6.0:", when="+python @0.7.0:")

    depends_on("mochi-thallium@0.12.0:", when="@0.2.0:")
    depends_on("mochi-margo@0.15.0:", when="@0.2.0:")
    depends_on("mochi-remi@0.4.0:", when="+remi @0.2.0:")
    depends_on("mochi-bedrock@0.8.0:0.14.2", when="+bedrock @0.2.0:0.3.0")

    depends_on("mochi-thallium@develop", when="@develop")
    depends_on("mochi-bedrock-module-api@develop", when="@develop +bedrock")
    depends_on("mochi-abt-io@develop", when="@develop")
    depends_on("mochi-remi@develop", when="@develop +remi")
    depends_on("py-mochi-margo@develop", when="+python @develop")

    depends_on("python", when="+python")
    depends_on("py-configspace@1.1.4:", when="+space")
    depends_on("mochi-bedrock+space", when="+space")

    extends("python", when="+python")

    def cmake_args(self):
        args = []
        variant_bool = lambda feature: str(feature in self.spec)
        args.append("-DENABLE_BEDROCK:BOOL=%s" % variant_bool("+bedrock"))
        args.append("-DENABLE_REMI:BOOL=%s" % variant_bool("+remi"))
        args.append("-DENABLE_PYTHON:BOOL=%s" % variant_bool("+python"))
        return args
