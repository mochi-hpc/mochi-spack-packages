##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack.package import *
from spack import *


class MochiPoesie(CMakePackage):
    """A Mochi library that provides a Margo-based embedded scripting service"""

    homepage = "https://github.com/mochi-hpc/mochi-poesie"
    url = "https://github.com/mochi-hpc/mochi-poesie/archive/refs/tags/v0.2.tar.gz"
    git = "https://github.com/mochi-hpc/mochi-poesie.git"

    version("develop", branch="main")
    version("main", branch="main")
    version("0.3.2", sha256="b7d5bee1e75e938cea9d5b3fecb1197de830a1d25d8a8e54ecbddef88a6d3e0a")
    version("0.3.1", sha256="07c0049199958dd91ce1402b67ded1467a6147c23805415ad38ac10f5400121b")
    version("0.3.0", sha256="e21c262242333097f892c332bd14409fc60d3bd3b66e1e71d1a1e0c33a07cba6")
    version("0.2", sha256="dafbdcdd8feb8d81f0dd31cc329c3656e22c8381b5c6a628e57567822190e9d3")

    variant("lua", default=True, description="Enable Lua interpreters")
    variant("python", default=True, description="Enable Python interpreters")
    variant("ruby", default=True, description="Enable Ruby interpreters", when="@main")
    variant("bedrock", default=True, description="Enable Bedrock support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("mochi-thallium@0.14.5:", when="@0.3.0:")

    depends_on("mochi-margo@0.9:", when="@0.2")
    depends_on("mochi-bedrock@:0.11.0", when="+bedrock @0.2")
    depends_on("mochi-bedrock-module-api@0.1.0", when="+bedrock @0.3.0")
    depends_on("mochi-bedrock-module-api@0.2.0:", when="+bedrock @0.3.1:")

    depends_on("mochi-thallium@develop", when="@develop")
    depends_on("mochi-margo@develop", when="@develop")
    depends_on("mochi-bedrock-module-api@develop", when="+bedrock @develop")

    depends_on("json-c")
    depends_on("lua", when="+lua @0.2")
    depends_on("lua-sol2", when="+lua @0.3.0:")
    depends_on("python@3.6:", when="+python @0.2")
    depends_on("py-pybind11", when="+python @0.3.0:")
    depends_on("mruby@3.3.0: cflags=-fPIC", when="+ruby @0.3.0:")
    depends_on("pkgconfig", type=("build",), when="@0.3.0:")
    depends_on("nlohmann-json", when="@0.3.0:")
    depends_on("nlohmann-json-schema-validator", when="@0.3.0:")
    depends_on("spdlog", when="@0.3.0:")
    depends_on("fmt", when="@0.3.0:")
    depends_on("tclap", type=("build",), when="@0.3.0:")

    def cmake_args(self):
        cmake_args = [
            self.define_from_variant("ENABLE_PYTHON", "python"),
            self.define_from_variant("ENABLE_LUA", "lua"),
            self.define_from_variant("ENABLE_RUBY", "ruby"),
            self.define_from_variant("ENABLE_BEDROCK", "bedrock"),
        ]
        return cmake_args
