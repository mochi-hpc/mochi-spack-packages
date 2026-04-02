# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class MercuryNaLibp2p(CMakePackage):
    """Mercury NA plugin using libp2p for transport."""

    homepage = "https://github.com/mochi-hpc/mercury-na-libp2p"
    git = "https://github.com/mochi-hpc/mercury-na-libp2p.git"

    maintainers("mdorier")

    license("MIT", checked_by="mdorier")

    version("main", branch="main")

    depends_on("cmake@3.15:", type="build")
    depends_on("rust@1.77:", type="build")
    depends_on("mercury@2.4:+plugins")
