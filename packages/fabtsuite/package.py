# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
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
#     spack install fabtsuite
#
# You can edit this file again by typing:
#
#     spack edit fabtsuite
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
from spack.package import *


class Fabtsuite(CMakePackage):
    """Fabtsuite is a test suite for libfabric."""

    homepage = "https://www.hdfgroup.org"
    git      = "https://github.com/mercury-hpc/fabtsuite.git"

    maintainers = ['hyoklee']

    version('main', branch='main')

    depends_on('libfabric')
