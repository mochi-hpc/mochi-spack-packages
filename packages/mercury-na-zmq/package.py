# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class MercuryNaZmq(CMakePackage):
    """Mercury NA plugin using ZeroMQ for transport."""

    homepage = "https://github.com/mochi-hpc/mercury-na-zmq"
    git = "https://github.com/mochi-hpc/mercury-na-zmq.git"

    maintainers("mdorier")

    license("MIT", checked_by="mdorier")

    version("main", branch="main")

    depends_on("cmake@3.15:", type="build")
    depends_on("mercury@2.4:+plugins")
    depends_on("libzmq")
    depends_on("toml11")
    depends_on("uuid")
    depends_on("pkgconfig")
