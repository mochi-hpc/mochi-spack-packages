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
    version("0.1.2", sha256="ad33d9068bcf5776878245b3ecc11f4be314ec4eadc2ad89397fbe4e2dd5719a")
    version("0.1.1", sha256="fc10556968ad047154fe524489e6585c3eb253940dfef20a02c80ffd23629013")
    version("0.1.0", sha256="7f90bfd82a6b453f699989a08f30bde4b771f2cfbcafe0197286104badec4569")

    variant("python", default=True, when="@0.0.3:",
            description="Enable python support")
    variant("mpi", default=True, when="@0.1.0:",
            description="Enable MPI support in Mofka and its dependencies")
    variant("benchmark", default=True, when="@0.1.0:",
            description="Enable building the Mofka benchmark")
    requires("+mpi", when="+benchmark",
             msg="+mpi variant is required to build the Mofka benchmark")

    extends("python", when="+python")

    depends_on("cmake@3.21:", type=("build",))
    depends_on("pkgconfig", type=("build",))
    depends_on("uuid")
    depends_on("spdlog")
    depends_on("fmt")
    depends_on("nlohmann-json")
    depends_on("nlohmann-json-schema-validator")

    depends_on("argobots@1.2:")

    depends_on("mochi-margo@0.17.1:")
    depends_on("mochi-thallium")

    # TODO depends_on("mochi-bedrock@0.15.0:", when="@0.2.0:")
    depends_on("mochi-bedrock@0.14.0:0.14.2", when="@0.1.2")
    depends_on("mochi-bedrock@0.12.0:0.14.2", when="@0.1.1:0.1.2")
    depends_on("mochi-bedrock@0.11.0:0.14.2", when="@main") # TODO remove
    depends_on("mochi-bedrock+mpi", when="+mpi")

    depends_on("mochi-yokan@0.6.0:+bedrock", when="@0.1.2:")
    depends_on("mochi-yokan@0.4.2:+bedrock")

    depends_on("mochi-warabi@0.5.0:+bedrock", when="@0.1.2:")
    depends_on("mochi-warabi@0.3.0:+bedrock")

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
        return args
