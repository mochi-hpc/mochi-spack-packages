# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
from spack.pkg.builtin.json_c import JsonC as BuiltinJsonC

class JsonC(BuiltinJsonC):

# this is only provided for compatibility with systems (like Polaris, as of
# 2023-12-4) that use a system json-c version 0.13 as a dependency in
# libfabric
    version('0.13.0', sha256='0316780be9ad16c42d7c26b015a784fd5df4b0909fef0aba51cfb13e492ac24d', url="https://s3.amazonaws.com/json-c_releases/releases/json-c-0.13.tar.gz")

