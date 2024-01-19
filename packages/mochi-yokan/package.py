# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *
from spack import *


class MochiYokan(CMakePackage):
    """A Mochi library that provides a Margo-based key/value service."""

    homepage = "https://github.com/mochi-hpc/mochi-yokan"
    url = "https://github.com/mochi-hpc/mochi-yokan/archive/refs/tags/v0.1.tar.gz"
    git = "https://github.com/mochi-hpc/mochi-yokan.git"

    version("develop", branch="main")
    version("main", branch="main")
    version("0.4.2", sha256="717c32c17d97edecd5f7d4b549aad18c079c421cc5bd502dcc1e70da0e11ec30")
    version("0.4.1", sha256="f394c7e19747f80a86e5ffd3326920625334a1004725bbd21c4d89f7aa89f20b")
    version("0.4.0", sha256="25397070d8322bc9ebfc5c866f9215c88f9fa9941f132518e3845232ae38b273")
    version("0.3.0", sha256="663ba390b98dc870be3db8beca6c76591838243c2669719d0e25e87b18851218")
    version("0.2.11", sha256="fd9eab5a176f795907c43a89b7a5660c7f62c5042ad49265c1c9aba125685ae0")
    version("0.2.10", sha256="621bf4aba02d3382eb8a3b8bf89bb7f790393da2ff5d7f023304d5062d68c2ab")
    version("0.2.9", sha256="8a8b6c614fc8f6afd890d95c8526f54571c8c0ddcd9e9e2557a6addbf837e096")
    version("0.2.8", sha256="2f89876d07f482b22f4bddc790f4830a264dc2c6f9dd701cb51c19f01dbd059e")
    version("0.2.7", sha256="ff32bf67c2d908acad872a2d9b8d077d1011c90367979d8ed8b03d47c586cfd4")
    version("0.2.6", sha256="0b4e60aa8241283c10edc136ddf69514f96e2ce08020fc5a5c38173b1e7bc9e2")
    version("0.2.5", sha256="e0663531fcf3e8ee3e290d5b28a31c54a1c57f45f67f4000ae23d9913705ff68")
    version("0.2.4", sha256="a81630b93a0172aab489c6069e723818a6fafcb3bde4efb96be7401b0f2d51f5")
    version("0.2.3", sha256="6e6f13d29d9a85ac34030298e6678c5a8834f5e627e46958c6be076ce1eebf60")
    version("0.2.2", sha256="b6c7a5caf664aeb9472cb37c3138251243cc47dc2f8688e22053588dab28cf40")
    version("0.2.1", sha256="d5731d2c83c37f231ef0026ed3df82f774b94dd365d75bb396ed68d1884288c3")
    version("0.2", sha256="aea3f435342a37c2f3332200fac8894ef78b0e6f2b200ec18be9f41389902f78")
    version("0.1", sha256="b5043ba37102e8956ae59201953e9e7ce56378dde19a4c99b6e82b9ff575d675")

    variant("remi", default=False, description="Enable migration with REMI",
            when="@0.4.0:")
    variant("berkeleydb", default=False, description="Enable BerkelyDB backend")
    variant("leveldb", default=False, description="Enable LevelDB backend")
    variant("lmdb", default=False, description="Enable LMDB backend")
    variant("rocksdb", default=False, description="Enable RocksDB backend")
    variant("tkrzw", default=False, description="Enable TKRZW backend")
    variant("gdbm", default=False, description="Enable GDBM backend")
    variant("unqlite", default=False, description="Enable Unqlite backend")
    variant("lua", default=False, description="Enable Lua filtering")
    variant("python", default=False, description="Enable Python binding")
    variant("bedrock", default=False, description="Enable Bedrock support")

    depends_on("cmake@3.15:", type="build")
    depends_on("pkgconfig")
    depends_on("uuid")
    depends_on("nlohmann-json")
    depends_on("tclap")

    # mochi dependencies
    depends_on("mochi-margo@0.15.0:", when="@0.4.0:")
    depends_on("mochi-margo@0.9.5:")
    depends_on("mochi-bedrock", when="+bedrock")
    depends_on("mochi-bedrock@0.8.0:", when="+bedrock @0.4.0:")
    depends_on("py-mochi-margo@0.4:", when="+python")
    depends_on("mochi-remi@0.4.0:", when="+remi")

    # mochi dependencies for develop version
    depends_on("mochi-margo@develop", when="@develop")
    depends_on("mochi-bedrock@develop", when="+bedrock @develop")
    depends_on("py-mochi-margo@develop", when="+python @develop")

    # backends
    depends_on("berkeley-db @18.1.40: +cxx +stl", when="+berkeleydb")
    # For now we are stuck with leveldb 1.22 because of a problem with 1.23
    # (see https://github.com/google/leveldb/issues/891)
    depends_on("leveldb@:1.22", when="+leveldb")
    depends_on("lmdb", when="+lmdb")
    depends_on("rocksdb", when="+rocksdb")
    depends_on("rocksdb+rtti", when="+rocksdb @0.2.9:")
    depends_on("rocksdb@:6", when="+rocksdb @:0.2.5")
    depends_on("tkrzw", when="+tkrzw")
    depends_on("gdbm", when="+gdbm")
    depends_on("unqlite@master", when="+unqlite")

    # additional dependencies
    depends_on("lua-sol2", when="+lua")
    depends_on("python@3.6.0:", when="+python")
    depends_on("py-pybind11@2.7.0:", when="+python")
    depends_on("py-pybind11@2.7.0:2.10.4", type=("build"), when="@:0.3.0 +python")

    extends("python", when="+python")

    def cmake_args(self):
        args = []
        variant_bool = lambda feature: str(feature in self.spec)
        args.append("-DENABLE_BERKELEYDB:BOOL=%s" % variant_bool("+berkeleydb"))
        args.append("-DENABLE_LEVELDB:BOOL=%s" % variant_bool("+leveldb"))
        args.append("-DENABLE_LMDB:BOOL=%s" % variant_bool("+lmdb"))
        args.append("-DENABLE_ROCKSDB:BOOL=%s" % variant_bool("+rocksdb"))
        args.append("-DENABLE_TKRZW:BOOL=%s" % variant_bool("+tkrzw"))
        args.append("-DENABLE_GDBM:BOOL=%s" % variant_bool("+gdbm"))
        args.append("-DENABLE_UNQLITE:BOOL=%s" % variant_bool("+unqlite"))
        args.append("-DENABLE_LUA:BOOL=%s" % variant_bool("+lua"))
        args.append("-DENABLE_PYTHON:BOOL=%s" % variant_bool("+python"))
        args.append("-DENABLE_BEDROCK:BOOL=%s" % variant_bool("+bedrock"))
        return args
