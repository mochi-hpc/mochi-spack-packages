# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class MochiFlock(CMakePackage):
    """Flock is a group membership microservice for Mochi."""

    url = "https://github.com/mochi-hpc/mochi-flock/archive/refs/tags/v0.1.0.tar.gz"
    homepage = "https://github.com:/mochi-hpc/mochi-flock"
    git = "https://github.com:/mochi-hpc/mochi-flock.git"

    maintainers("mdorier")

    version("main", branch="main")
    version("develop", branch="main")
    version("0.1.0", sha256="5bf3a87ad3f1408f322e9e777f96ad7a82c26b93dcf1df6ba4bffa11a55dc2ee")

    variant("bedrock", default=False, description="Enable Bedrock support")
    variant("mpi", default=False, description="Enable MPI support")

    depends_on("pkgconfig", type=("build",))
    depends_on("mochi-margo")
    depends_on("json-c")

    depends_on("mochi-bedrock", when="+bedrock")

    depends_on("mochi-margo@develop", when="@develop")
    depends_on("mochi-bedrock@develop", when="@develop +bedrock")

    def cmake_args(self):
        args = []
        variant_bool = lambda feature: str(feature in self.spec)
        args.append("-DENABLE_BEDROCK:BOOL=%s" % variant_bool("+bedrock"))
        args.append("-DENABLE_MPI:BOOL=%s" % variant_bool("+mpi"))
        return args
