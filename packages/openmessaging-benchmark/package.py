# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
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
#     spack install openmessaging-benchmark
#
# You can edit this file again by typing:
#
#     spack edit openmessaging-benchmark
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from spack.util.executable import which


class OpenmessagingBenchmark(MavenPackage):
    """ OpenMessaging Benchmark Framework is a benchmark for evaluating the
    performance of a number of messaging/streaming systems."""

    homepage = "https://openmessaging.cloud"
    git = "https://github.com/openmessaging/benchmark.git"

    maintainers("mdorier")

    license("Apache-2.0", checked_by="mdorier")

    version("master", branch="master")

    depends_on("java", type=("build", "run"))
    depends_on("maven@3.8.6:", type="build")

    def build_args(self):
        return ['-Dmaven.repo.local=' + self.prefix + '/.m2']
