# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.builtin.pmdk import Pmdk as BuiltinPmdk
from spack.package import *


class Pmdk(BuiltinPmdk):

    depends_on('cmake', type='build')
    depends_on('gmake', type='build')
