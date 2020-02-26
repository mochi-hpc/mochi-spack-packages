# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.mercury import Mercury

class Mercury(Mercury):

    git = 'https://github.com/mercury-hpc/mercury.git'
    version('2.0.0a1', tag='v2.0.0a1', submodules=True)
