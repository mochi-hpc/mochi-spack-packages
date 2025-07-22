# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class DiasporaStreamApi(CMakePackage):
    """An API for distributed event-streaming service for HPC."""

    url = "https://github.com/diaspora-project/diaspora-stream-api/archive/refs/tags/v0.0.1.tar.gz"
    homepage = "https://github.com/mdiaspora-project/diaspora-stream-api"
    git = "https://github.com/diaspora-project/diaspora-stream-api.git"

    maintainers("mdorier")

    version("main", branch="main")
    version("develop", branch="main")

    variant("python", default=True, when="@0.0.3:",
            description="Enable python support")

    extends("python", when="+python")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.21:", type=("build",))
    depends_on("pkgconfig", type=("build",))
    depends_on("nlohmann-json")
    depends_on("nlohmann-json-schema-validator")

    with when("+python"):
        depends_on("py-pybind11", type=("build",))

    def cmake_args(self):
        args = []
        if "+python" in self.spec:
            args.append("-DENABLE_PYTHON=ON")
        else:
            args.append("-DENABLE_PYTHON=OFF")
        return args
