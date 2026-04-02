# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install c-libp2p
#
# You can edit this file again by typing:
#
#     spack edit c-libp2p
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class CLibp2p(CMakePackage):
    """C implementation of Libp2p ."""

    homepage = "https://libp2p.io/"
    git = "https://github.com/Pier-Two/c-libp2p.git"

    maintainers("mdorier")

    license("MIT", checked_by="mdorier")

    version("main", branch="main", submodules=True)

    depends_on("cmake@3.10:", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("openssl")

    def cmake_args(self):
        return ["-DENABLE_COVERAGE=OFF"]
