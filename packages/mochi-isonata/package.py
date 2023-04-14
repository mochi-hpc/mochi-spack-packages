# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class MochiIsonata(CMakePackage):
    """Interface to swap Sonata for alternative implementations"""

    homepage = "https://github.com/mochi-hpc/mochi-isonata"
    url = "https://github.com/mochi-hpc/mochi-isonata/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/mochi-hpc/mochi-isonata.git"

    version("main", branch="main")
    version("0.1.0", sha256="86ea6e0da391de9ff30023dc43096a1bf6ffb5ca1979a5371e0f37e24430dec4")

    variant("sonata", default=True, description="Enable Sonata backend")

    depends_on("mochi-thallium")
    depends_on("nlohmann-json")
    depends_on("mochi-sonata@0.6.3:", when="+sonata")

    def cmake_args(self):
        args = []
        if "+sonata" in self.spec:
            args.append("-DENABLE_SONATA=ON")
        else:
            args.append("-DENABLE_SONATA=OFF")
        return args
