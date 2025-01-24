# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
import platform

_base_url = "https://dl.redpanda.com/nzc4ZYQK3WRGd9sy/redpanda/raw/names/"

_versions = {
    "24.2.7": {
        "Linux-x86_64": (
            "c1ff30bac25e27006b5fa20b356c898ca606dc9b9a1d171bf75b290d05ac4a19",
            _base_url + "redpanda-amd64/versions/24.2.7/redpanda-24.2.7-amd64.tar.gz"
        ),
        "Linux-aarch64": (
            "2c98d0a32eeabc3df5251982837a6bfa7e6f0f633e330fa019f6490ce4a686db",
            _base_url + "redpanda-arm64/versions/24.2.7/redpanda-24.2.7-arm64.tar.gz"
        )
    }
}
_target = platform.uname().machine

class Redpanda(Package):
    """Redpanda is a streaming data platform for developers. Kafka API compatible."""

    homepage = "https://www.redpanda.com/"
    url = _versions["24.2.7"][f"Linux-{_target}"][1]

    for ver, pkg in _versions.items():
        _checksum, _url = pkg[f"Linux-{_target}"]
        version(ver, sha256=_checksum, url=_url, expand=False)

    depends_on("patchelf", type="build")
    depends_on("tar", type="build")

    def install(self, spec, prefix):
        import os
        # Untar the downloaded archive
        with working_dir(prefix):
            tar = which("tar")
            tar("xvf", self.stage.archive_file)
        # Rename "lib" into "_lib" to avoid poluting LD_LIBRARY_PATH
        os.rename(join_path(prefix, "lib"), join_path(prefix, "redpanda_lib"))
        os.rename(join_path(prefix, "libexec"), join_path(prefix, "redpanda_libexec"))
        # Replace all instances of "/opt/redpanda" in all files
        # in the bin directory with the installation prefix
        bin_dir = join_path(prefix, 'bin')
        for file_name in os.listdir(bin_dir):
            file_path = join_path(bin_dir, file_name)
            filter_file('/opt/redpanda/lib', join_path(prefix, "redpanda_lib"), file_path)
            filter_file('/opt/redpanda', prefix, file_path)
        # Call patchelf do edit linker setting
        libexec_dir = join_path(prefix, 'redpanda_libexec')
        patchelf = which('patchelf')
        for file_name in os.listdir(libexec_dir):
            # NOTE: to be more generic, we should use "file <file_name>" to check
            # if the file is a dynamically linked ELF executable
            if file_name in ["test.sh", "rpk"]:
                continue
            file_path = join_path(libexec_dir, file_name)
            patchelf('--set-interpreter', join_path(prefix, 'redpanda_lib', 'ld.so'), file_path)
