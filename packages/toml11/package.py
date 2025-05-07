# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


try:
    from spack_repo.builtin.packages.toml11.package import Toml11 as BuiltinToml11
except ImportError:
    from spack.pkg.builtin.toml11 import Toml11 as BuiltinToml11
from spack.package import *


class Toml11(BuiltinToml11):

    version("4.0.2", sha256="d1bec1970d562d328065f2667b23f9745a271bf3900ca78e92b71a324b126070")
    version("4.0.1", sha256="96965cb00ca7757c611c169cd5a6fb15736eab1cd1c1a88aaa62ad9851d926aa")
    version("4.0.0", sha256="f3dc3095f22e38745a5d448ac629f69b7ee76d2b3e6d653e4ce021deb7f7266e")

    @when("@3.8.0:")
    def cmake_args(self):
        args = [self.define_from_variant("CMAKE_CXX_STANDARD", "cxx_std")]
        return args
