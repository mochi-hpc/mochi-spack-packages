##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
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
#
# Installing py-ssg:
#
#     spack install py-ssg
#
from spack import *
from spack.package import *


class PyMochiSsg(PythonPackage):
    """Python wrapper for the Mochi SSG library"""

    homepage = "https://github.com/mochi-hpc/py-mochi-ssg"
    url      = "https://github.com/mochi-hpc/py-mochi-ssg/archive/refs/tags/v0.2.0.tar.gz"
    git      = "https://github.com/mochi-hpc/py-mochi-ssg.git"

    version("develop", branch="main")
    version("main", branch="main")
    version("0.2.0", sha256="e1327f51b974476d253d6edc755de958bdc16451f1dd063e7e29c2819e8c659c")
    version("0.1.2", tag="v0.1.2")
    version("0.1.1", tag="v0.1.1")
    version("0.1", tag="v0.1")

    variant("mpi", default=True, description="Enable MPI support")
    variant("drc", default=False, description="Enable Cray-DRC support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("py-pkgconfig", type=("build"))
    depends_on("py-pybind11", type=("build"))
    depends_on('py-pybind11@:2.10.4', type=('build'), when='@:0.2.0')
    depends_on("py-setuptools", type=("build"))
    depends_on("py-mpi4py", when="+mpi")
    depends_on("mpi", when="+mpi", type=("build"))

    depends_on("mochi-ssg+mpi@0.5.3:", when="@0.2.0: +mpi")
    depends_on("mochi-ssg@0.5.3:", when="@0.2.0: ~mpi")
    depends_on("mochi-ssg+mpi@0.4.1:0.4.5", when="@0.1.2 +mpi")
    depends_on("mochi-ssg@0.4.1:0.4.5", when="@0.1.2 ~mpi")
    depends_on("mochi-ssg+mpi@0.1:0.2", when="@0.1:0.1.1 +mpi")
    depends_on("mochi-ssg@0.1:0.2", when="@0.1:0.1.1 ~mpi")
    depends_on("py-mochi-margo@0.1:")

    depends_on("mochi-ssg+mpi@develop", when="+mpi @develop")
    depends_on("mochi-ssg@develop", when="~mpi @develop")
    depends_on("py-mochi-margo@develop", when="@develop")

    depends_on("rdma-credentials", when="+drc")

    def setup_build_environment(self, env):
        if "+mpi" in self.spec:
            env.set("CC", self.spec["mpi"].mpicc)
            env.set("CXX", self.spec["mpi"].mpicxx)
