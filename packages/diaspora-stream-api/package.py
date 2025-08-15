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
    version("0.2.0", sha256="e72bd78401ba480c895a4897a1d0c618433ad7a729fd3badefa7250567921672")
    version("0.1.0", sha256="e61b776300ab6f61d34dbb7cee115f2ca64f05f73f2719e730f0debe1f8f1594")

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
