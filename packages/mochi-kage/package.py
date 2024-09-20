# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class MochiKage(CMakePackage):
    """Kage is a proxy microservice for Mochi."""

    url = "https://github.com/mochi-hpc/mochi-kage/archive/refs/tags/v0.1.0.tar.gz"
    homepage = "https://github.com:/mochi-hpc/mochi-kage"
    git = "https://github.com:/mochi-hpc/mochi-kage.git"

    maintainers("mdorier")

    version("main", branch="main")
    version("develop", branch="main")

    variant("bedrock", default=True, description="Enable Bedrock support")
    variant("zmq", default=True, description="Enable ZeroMQ support")

    depends_on("pkgconfig", type=("build",))
    depends_on("nlohmann-json")
    depends_on("nlohmann-json-schema-validator@2.3.0:", when="@0.3.0:")
    depends_on("spdlog")
    depends_on("fmt")
    depends_on("cppzmq", when="+zmq")

    depends_on("mochi-thallium@0.13.1:")
    depends_on("mochi-bedrock-module-api@0.2.0:", when="+bedrock")
    # TODO depends_on("mercury@2.4.0:") # need HG_Get_in/output_payload_size
    depends_on("mercury@2.4.0rc5", when="@main") # TODO when 2.4.0 is released, delete and uncomment above

    depends_on("mochi-thallium@develop", when="@develop")
    depends_on("mochi-bedrock-module-api@develop", when="@develop +bedrock")

    def cmake_args(self):
        args = []
        variant_bool = lambda feature: str(feature in self.spec)
        args.append("-DENABLE_BEDROCK:BOOL=%s" % variant_bool("+bedrock"))
        args.append("-DENABLE_ZMQ:BOOL=%s" % variant_bool("+zmq"))
        return args
