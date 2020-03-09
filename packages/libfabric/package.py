# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.libfabric import Libfabric

class Libfabric(Libfabric):

    version('1.9.1', sha256='c305c6035c992523e08c7591a6a3707225ba3e72de40443eaed837a10df6771a', preferred=True)
