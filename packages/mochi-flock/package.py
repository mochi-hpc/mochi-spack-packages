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
    version("0.7.0", sha256="a45630c7319fd55ec897a396de2ef367387608de22e871ef6b1722c71c9598cd")
    version("0.6.0", sha256="1bd7bd54fd7a4b5f84006eadaab3f911c78afb50ec723385ad3a8f6edef2e8ac")
    version("0.5.3", sha256="c31cd09b7e41b31267d5825e5ea31122d4354dfe715ea1f92363a9d976e4de4d")
    version("0.5.2", sha256="8ef27766ba449503dff9dd9fd58619977820e0f0fc833555193c4384a2a60d96")
    version("0.5.1", sha256="5f91515f9997342c8d4f2f212e08f3345d1927c46ffd88cadb27a0dc144cdc7e")
    version("0.5.0", sha256="88cb8d5794d8451c7595f785cbaaf1d57870a44bd86f799f5e48534178a1bcd2")
    version("0.4.1", sha256="d6ec1ebcc9721aeda32dbf18cd7f50f9ce3e2364169bf455df44549c6b2ef55a")
    version("0.4.0", sha256="42508939ac7c65da2627d2af59bdad0e456c12f6593b49a0a45a0e651e56c5f9")
    version("0.3.1", sha256="6f589f7f43b31bbe004ebc7672fe52398540243d7ea825aed9aa204f2de423b0")
    version("0.3.0", sha256="e7aa78e01ce952731a91a703275deb398b46280e960d35227e350b9fb238dc38")
    version("0.2.2", sha256="7b66503b9bd96245ec918c97f142443969725bb151c761dc2cbd41f583b0417c")
    version("0.2.1", sha256="0cd25bc32ffccc5a4249c49d2a874b9d1a1a7f15d428b17e3ecadc6e2661a14d")
    version("0.2.0", sha256="fce7ecb61f7ec9f8e3f5929427943d001ce66800979d4b125f9647162004d6b6")
    version("0.1.0", sha256="5bf3a87ad3f1408f322e9e777f96ad7a82c26b93dcf1df6ba4bffa11a55dc2ee")

    variant("bedrock", default=True, description="Enable Bedrock support")
    variant("mpi", default=False, description="Enable MPI support")
    variant("python", default=False, description="Enable Python support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("pkgconfig", type=("build",))
    depends_on("json-c")
    depends_on("py-pybind11", when="@0.2.0: +python")
    depends_on("mochi-margo")
    depends_on("mochi-thallium", when="@0.2.0:")
    depends_on("py-mochi-margo", when="@0.2.0: +python")
    depends_on("py-mochi-margo@0.6.1:", when="@0.5.3: +python")
    depends_on("mochi-bedrock@:0.14.2", when="+bedrock @:0.2.2")
    depends_on("mochi-bedrock-module-api@0.1.0:", when="+bedrock @0.3.0:")
    depends_on("mochi-bedrock-module-api@0.2.0:", when="+bedrock @0.5.0:")

    depends_on("mochi-margo@develop", when="@develop")
    depends_on("mochi-bedrock-module-api@develop", when="@develop +bedrock")
    depends_on("mochi-thallium@develop", when="@develop")
    depends_on("py-mochi-margo@develop", when="@develop +python")

    def cmake_args(self):
        args = []
        variant_bool = lambda feature: str(feature in self.spec)
        args.append("-DENABLE_BEDROCK:BOOL=%s" % variant_bool("+bedrock"))
        args.append("-DENABLE_MPI:BOOL=%s" % variant_bool("+mpi"))
        args.append("-DENABLE_PYTHON:BOOL=%s" % variant_bool("+python"))
        if "+mpi" in self.spec:
            args.append("-DCMAKE_CXX_COMPILER="+self.spec["mpi"].mpicxx)
            args.append("-DCMAKE_C_COMPILER="+self.spec["mpi"].mpicc)
        return args
