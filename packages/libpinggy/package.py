# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Libpinggy(CMakePackage):
    """Core SDK for the Pinggy tunnel service."""

    url = "https://github.com/Pinggy-io/libpinggy/archive/refs/tags/v0.1.4.tar.gz"
    homepage = "https://pinggy.io/"
    git = "https://github.com/Pinggy-io/libpinggy.git"

    maintainers("mdorier")

    version("main", branch="main", get_full_repo=True)
    #version("0.1.4", sha256="abb15be7e32ce131cb4576641feabffda663ab02f09a30400c4e072a5fa317ce")
    version("0.1.4", tag="v0.1.4", get_full_repo=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("git", type=("build",))
    depends_on("cmake@3.15:", type=("build",))
    depends_on("openssl@3.0.3:")
