# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class MochiFlock(CMakePackage):
    """Flock is a group membership microservice for Mochi."""

    url = "https://github.com/mochi-hpc/mochi-flock/archive/refs/tags/v0.1.0.tar.gz"
    homepage = "https://github.com:/mochi-hpc/mochi-flock"
    git = "https://github.com:/mochi-hpc/mochi-flock.git"

    maintainers("mdorier")

    version("main", branch="main")
    version("develop", branch="main")
    version("0.3.0", sha256="e7aa78e01ce952731a91a703275deb398b46280e960d35227e350b9fb238dc38")
    version("0.2.2", sha256="7b66503b9bd96245ec918c97f142443969725bb151c761dc2cbd41f583b0417c")
    version("0.2.1", sha256="0cd25bc32ffccc5a4249c49d2a874b9d1a1a7f15d428b17e3ecadc6e2661a14d")
    version("0.2.0", sha256="fce7ecb61f7ec9f8e3f5929427943d001ce66800979d4b125f9647162004d6b6")
    version("0.1.0", sha256="5bf3a87ad3f1408f322e9e777f96ad7a82c26b93dcf1df6ba4bffa11a55dc2ee")

    variant("bedrock", default=True, description="Enable Bedrock support")
    variant("mpi", default=False, description="Enable MPI support")
    variant("python", default=False, description="Enable Python support")

    depends_on("pkgconfig", type=("build",))
    depends_on("json-c")
    depends_on("py-pybind11", when="@0.2.0: +python")
    depends_on("mochi-margo")
    depends_on("mochi-thallium", when="@0.2.0:")
    depends_on("py-mochi-margo", when="@0.2.0: +python")
    depends_on("mochi-bedrock", when="+bedrock @:0.2.2")
    depends_on("mochi-bedrock-module-api", when="+bedrock @0.3.0:")

    depends_on("mochi-margo@develop", when="@develop")
    depends_on("mochi-bedrock@develop", when="@develop +bedrock")
    depends_on("mochi-thallium@develop", when="@develop")
    depends_on("py-mochi-margo@develop", when="@develop +python")

    def cmake_args(self):
        args = []
        variant_bool = lambda feature: str(feature in self.spec)
        args.append("-DENABLE_BEDROCK:BOOL=%s" % variant_bool("+bedrock"))
        args.append("-DENABLE_MPI:BOOL=%s" % variant_bool("+mpi"))
        args.append("-DENABLE_PYTHON:BOOL=%s" % variant_bool("+python"))
        return args
