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
    version("0.6.3", sha256="80fad71e621be86d4c9a162d4e327b2f3d5fca424a20f3dab74d8bdbf9efc420")
    version("0.6.2", sha256="6d3d49b2be69d6a66febdeebf12acc223458d2545b475ac19d97852c87c1a91e")
    version("0.6.1", sha256="cbb1b82e13c1787c629dcc113ff0c009ba47a3cbe058ab1be39bff9e5e2faa93")
    version("0.6.0", sha256="02fcf6cfb36dc58c2509a3cc07ab9193683dc0fe3174376c6003fad051e4d2e9")
    version("0.5.3", sha256="0b30e6cf4cb0b567945970c0014e6bf00138d46b3d160f24c78d6159dd9dd22a")
    version("0.5.2", sha256="53015cb060e9c1f89a292a6648c266e1b9eff1d51301d15b4735e9b7092f2bad")
    version("0.5.1", sha256="b5fadba1e304e10ec4e1438dcf18fb723664f9c769f064017189d3688ff2b8cf")
    version("0.5.0", sha256="97d932f6daa1b367d57f8eaf05299244fb949dbe533d195b04a4ef3ba6e6e217")
    version("0.4.0", sha256="e58754d35a9ec9f6b7df43942f8b8887c65e1ff025078c15d045cbe5590f2ee3")
    version("0.3.3", sha256="bd814287a60ae045deea52c4b1843ae59b6017497096242f8143d3ffd3843466")
    version("0.3.2", sha256="6fcbe81487093e111cba82d7d7fd8ec82190e27f8309446e0164d6ff84608ff3")
    version("0.3.1", sha256="b60811e023ad57ada70b68ea1dbabeeac020930b72a37013fec6b36827db52ce")
    version("0.3.0", sha256="6489051756444a53b175ced040a10a4acaa942df5fe92c1f8e22b45f50537436")
    version("0.2.0", sha256="038ce14a8643ff143311616adf7e0ade6bdf47448012b13e3417e53167f8bbee")
    version("0.1.2", sha256="ad33d9068bcf5776878245b3ecc11f4be314ec4eadc2ad89397fbe4e2dd5719a")
    version("0.1.1", sha256="fc10556968ad047154fe524489e6585c3eb253940dfef20a02c80ffd23629013")
    version("0.1.0", sha256="7f90bfd82a6b453f699989a08f30bde4b771f2cfbcafe0197286104badec4569")

    variant("python", default=True, when="@0.0.3:",
            description="Enable python support")
    variant("mpi", default=True, when="@0.1.0:",
            description="Enable MPI support in Mofka and its dependencies")
    variant("benchmark", default=False, when="@0.1.0:",
            description="Enable building the Mofka benchmark")
    variant("kafka", default=False, when="@0.3.0:",
            description="Enable Kafka support")
    requires("+mpi", when="+benchmark",
             msg="+mpi variant is required to build the Mofka benchmark")

    extends("python", when="+python")

    depends_on("cmake@3.21:", type=("build",))
    depends_on("pkgconfig", type=("build",))
    depends_on("curl", when="@0.3.0")
    depends_on("uuid")
    depends_on("spdlog")
    depends_on("fmt")
    depends_on("nlohmann-json")
    depends_on("nlohmann-json-schema-validator")

    depends_on("argobots@1.2:")

    depends_on("mochi-margo@0.17.1:")
    depends_on("mochi-margo@0.18.3:", when="@0.4.0:")
    depends_on("mochi-margo@0.19.1:", when="@0.5.3:")
    depends_on("mochi-thallium")

    depends_on("mochi-bedrock@0.15.0:", when="@0.2.0:")
    depends_on("mochi-bedrock@0.14.0:0.14.2", when="@0.1.2")
    depends_on("mochi-bedrock@0.12.0:0.14.2", when="@0.1.1:0.1.2")
    depends_on("mochi-bedrock+mpi", when="+mpi")

    depends_on("mochi-yokan@0.8.0:+bedrock", when="@0.4.1:")
    depends_on("mochi-yokan@0.7.0:+bedrock", when="@0.2.0:")
    depends_on("mochi-yokan@0.6.0:+bedrock", when="@0.1.2:")
    depends_on("mochi-yokan@0.4.2:+bedrock")

    depends_on("mochi-warabi@0.6.0:+bedrock", when="@0.2.0:")
    depends_on("mochi-warabi@0.5.0:+bedrock", when="@0.1.2:")
    depends_on("mochi-warabi@0.3.0:+bedrock")

    depends_on("mochi-flock@0.5.0:+bedrock", when="@0.2.0:")
    depends_on("mochi-flock@0.2.2:+bedrock")
    depends_on("mochi-flock@0.2.2:+mpi", when="+mpi")

    with when("+python"):
        depends_on("mochi-bedrock+python")
        depends_on("mochi-flock+python", when="@0.1.0:")
        depends_on("mochi-yokan+python")
        depends_on("mochi-warabi+python")
        depends_on("py-mochi-margo")
        depends_on("py-pybind11", type=("build",))
        depends_on("py-typer")
        depends_on("py-rich")

    with when("+kafka"):
        depends_on("kafka")
        depends_on("librdkafka")

    with when("+benchmark"):
        depends_on("mochi-bedrock+space")
        depends_on("mochi-yokan+space")
        depends_on("mochi-warabi+space")

    with when("@develop"):
        depends_on("mochi-thallium@develop")
        depends_on("mochi-bedrock@develop")
        depends_on("mochi-yokan@develop")
        depends_on("mochi-warabi@develop")
        depends_on("py-mochi-margo@develop", when="+python")
        depends_on("mochi-flock@develop")

    def cmake_args(self):
        args = []
        if "+mpi" in self.spec:
            args.append("-DCMAKE_CXX_COMPILER="+self.spec["mpi"].mpicxx)
            args.append("-DCMAKE_C_COMPILER="+self.spec["mpi"].mpicc)
        if self.spec.satisfies("@0.0.1"):
            args.append("-DENABLE_BAKE=OFF")
        if "+python" in self.spec:
            args.append("-DENABLE_PYTHON=ON")
        else:
            args.append("-DENABLE_PYTHON=OFF")
        if "+benchmark" in self.spec:
            args.append("-DENABLE_BENCHMARK=ON")
        else:
            args.append("-DENABLE_BENCHMARK=OFF")
        if "+kafka" in self.spec:
            args.append("-DENABLE_KAFKA=ON")
        else:
            args.append("-DENABLE_KAFKA=OFF")
        return args
