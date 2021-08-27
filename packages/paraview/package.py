# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.paraview import Paraview

class Paraview(Paraview):

    variant('mochi', default=False,
            description='Patch the source to enable non-MPI communicators')

    patch('disable-force-mpi-for-parallel-comm.patch', when="+mochi")

    def cmake_args(self):
        args = super(Paraview, self).cmake_args()
        if '+mochi' in self.spec:
            args.remove('-DPARAVIEW_BUILD_WITH_EXTERNAL=ON')
            args.append('-DPARAVIEW_BUILD_WITH_EXTERNAL=OFF')
        return args
