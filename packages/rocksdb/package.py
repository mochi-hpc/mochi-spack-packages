# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.rocksdb.package import Rocksdb as BuiltinRocksdb
except ImportError:
    from spack.pkg.builtin.rocksdb import Rocksdb as BuiltinRocksdb

class Rocksdb(BuiltinRocksdb):

    variant("rtti", default=False, description="Build with RTTI")

    def install(self, spec, prefix):
        if "+rtti" in spec:
            env["USE_RTTI"] = "1"
        super().install(spec, prefix)
