# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
from spack.package import *


class MochiIsonata(CMakePackage):
    """Interface to swap Sonata for alternative implementations"""

    homepage = "https://github.com/mochi-hpc/mochi-isonata"
    url = "https://github.com/mochi-hpc/mochi-isonata/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/mochi-hpc/mochi-isonata.git"

    version("main", branch="main")
    version("0.2.0", sha256="2266b2afac2de7befb15b696c9613b1b7a25a700c378687feab5644cabde7b8c")
    version("0.1.0", sha256="86ea6e0da391de9ff30023dc43096a1bf6ffb5ca1979a5371e0f37e24430dec4")

    variant("sonata", default=True, description="Enable Sonata backend")
    variant("yokan", default=True, description="Enable Yokan backend",
            when="@0.2.0:")

    depends_on("mochi-thallium")
    depends_on("nlohmann-json")
    depends_on("mochi-sonata@0.6.3:", when="+sonata")
    depends_on("mochi-yokan@0.2.11:", when="+yokan")

    def cmake_args(self):
        args = [
            self.define_from_variant("ENABLE_SONATA", "sonata"),
            self.define_from_variant("ENABLE_YOKAN", "yokan")
        ]
        return args
