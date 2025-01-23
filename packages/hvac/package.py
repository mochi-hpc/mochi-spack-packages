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
#     spack install hvac
#
# You can edit this file again by typing:
#
#     spack edit hvac
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Hvac(CMakePackage):
    """
    High-Velocity AI Cache (HVAC), a distributed read-cache layer that
    targets and fully exploits the node-local storage or near node-local
    storage technology. HVAC seamlessly accelerates read I/O by aggregating
    node-local or near node-local storage, avoiding metadata lookups and
    file locking while preserving portability in the application code.
    """

    homepage = "https://code.ornl.gov/42z/hvac-high-velocity-ai-cache"
    git = "https://code.ornl.gov/42z/hvac-high-velocity-ai-cache.git"

    version("main", branch="main")

    depends_on("mercury@2.0.0:")
    depends_on("libfabric@1.15.2.0:")
    depends_on("log4c")
    depends_on("cmake@3.10.2:", type="build")

    patch("001-fix-link-errors.patch")
