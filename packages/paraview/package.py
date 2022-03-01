# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.paraview import Paraview as BuiltinParaview

class Paraview(BuiltinParaview):

    variant('mochi', default=False,
            description='Patch the source to enable non-MPI communicators')

    patch('disable-force-mpi-for-parallel-comm.patch', when="+mochi")

    conflicts('@:5.7.99,5.8.1:', when='+mochi') # +mochi only applies to 5.8.0

    def cmake_args(self):
        args = super(Paraview, self).cmake_args()
        if '+mochi' in self.spec:
            args.remove('-DPARAVIEW_BUILD_WITH_EXTERNAL=ON')
            args.append('-DPARAVIEW_BUILD_WITH_EXTERNAL=OFF')
            args.append('-DVTK_PYTHON_OPTIONAL_LINK=OFF')
        return args

    def install(self, spec, prefix):
        super(Paraview, self).install(spec, prefix)
        if '+mochi' in spec:
            install('ThirdParty/IceT/vtkicet/src/include/*.h',
                    prefix.include+'/paraview-5.8')
