# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class DiasporaStreamApi(CMakePackage):
    """An API for distributed event-streaming service for HPC."""

    url = "https://github.com/diaspora-project/diaspora-stream-api/archive/refs/tags/v0.1.0.tar.gz"
    homepage = "https://github.com/mdiaspora-project/diaspora-stream-api"
    git = "https://github.com/diaspora-project/diaspora-stream-api.git"

    maintainers("mdorier")

    version("main", branch="main")
    version("develop", branch="main")
    version("0.4.0", sha256="0201c618057fc5e870f893a6431d4374af2cf62d1159950911d74d225a51f415")
    version("0.3.1", sha256="97df579851122dc832e3aa6d1a0f0846b6a2df133b19d9813e6ead878a5efe73")
    version("0.3.0", sha256="6b348e54650e7248c3dd56321f50803248cf6e14b3ea16c17d11baafea794811")
    version("0.2.0", sha256="e72bd78401ba480c895a4897a1d0c618433ad7a729fd3badefa7250567921672")
    version("0.1.0", sha256="e61b776300ab6f61d34dbb7cee115f2ca64f05f73f2719e730f0debe1f8f1594")

    variant("python", default=True, when="@0.3.0:",
            description="Enable python support")
    variant("tests", default=True, when="@0.3.0:",
            description="Build and install test suite")
    variant("benchmarks", default=True, when="@0.3.0:",
            description="Build and install the benchmarks")

    extends("python", when="+python")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.21:", type=("build",))
    depends_on("pkgconfig", type=("build",))
    depends_on("nlohmann-json")
    depends_on("nlohmann-json-schema-validator")

    with when("+tests"):
        depends_on("catch2@3.6.0:")

    with when("+python"):
        depends_on("py-pybind11", type=("build",))

    with when("+benchmarks"):
        depends_on("mpi")
        depends_on("tclap", type=("build",))

    def cmake_args(self):
        args = [
            self.define_from_variant("ENABLE_PYTHON", "python"),
            self.define_from_variant("ENABLE_TESTS", "tests"),
            self.define_from_variant("ENABLE_BENCHMARKS", "benchmarks"),
        ]
        if "+mpi" in self.spec:
            args.append("-DCMAKE_CXX_COMPILER="+self.spec["mpi"].mpicxx)
            args.append("-DCMAKE_C_COMPILER="+self.spec["mpi"].mpicc)
        return args
