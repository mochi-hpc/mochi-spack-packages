# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


try:
    from spack_repo.builtin.packages.pmdk.package import Pmdk as BuiltinPmdk
except:
    from spack.pkg.builtin.pmdk import Pmdk as BuiltinPmdk
from spack.package import *


class Pmdk(BuiltinPmdk):

    depends_on('cmake', type='build')
    depends_on('gmake', type='build')
