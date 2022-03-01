# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.libfabric import Libfabric as BuiltinLibfabric

class Libfabric(BuiltinLibfabric):

    # NOTE: some of these are duplicated in the upstream Spack package depending
    # on what version of Spack you are using.
    version('main', branch='main')
    version('1.13.2', sha256='25d783b0722a8df8fe61c1de75fafca684c5fe520303180f26f0ad6409cfc0b9')
    version('1.13.0', sha256='0c68264ae18de5c31857724c754023351614330bd61a50b40cef2b5e8f63ab28')
    version('1.12.1', sha256='db3c8e0a495e6e9da6a7436adab905468aedfbd4579ee3da5232a5c111ba642c')
    version('1.12.0', sha256='ca98785fe25e68a26c61e272be64a1efeea37e61b0dcebd34ccfd381bda7d9cc')
    version('1.11.2', sha256='ff2ba821b55a54855d327e6f6fb8a14312c9c9ca7c873525b6a246d8f974d7da')
    version('1.11.1', sha256='a72a7dac6322bed09ef1af33bcade3024ca5847a1e9c8fa369da6ab879111fe7')

    # this is a local variant used to safety check if spinlocks are causing
    # any deadlocks under heavy multithreaded workloads
    variant('disable-spinlocks', default=False, description='Replace all spin locks with mutex locks')
    conflicts('+disable-spinlocks', when='@:9999.99',
              msg='+disable-spinlocks variant only available for @master')

    patch('libfabric-1.11-option-disable-spinlocks.patch', when="+disable-spinlocks")


    # overriding the inherited class member has unusual side effects
    # ==> Error: module 'spack' has no attribute 'Libfabric'
    # so we'll copy 'fabrics' and add cxi ourselves.
    fabrics = ('efa',
               'gni',
               'mlx',
               'mrail',
               'psm',
               'psm2',
               'psm3',
               'rxm',
               'rxd',
               'shm',
               'sockets',
               'tcp',
               'udp',
               'usnic',
               'verbs',
               'xpmem',
               'cxi')

    # need to copy this blurb from builtin libfabric, else get an error:
    # ``` invalid values for variant "fabrics" ```
    variant('fabrics',
            default='sockets,tcp,udp',
            description='A list of enabled fabrics',
            values=fabrics,
            multi=True)

    def configure_args(self):
        spec = self.spec
        config_args = super(Libfabric, self).configure_args()

        # temporarily force-disable psm3 to make sure that it doesn't interfere on newer builds
        config_args.append('--disable-psm3')

        if '+disable-spinlocks' in spec:
            config_args.append('--disable-spinlocks')
        return config_args

    depends_on('m4', when='@main', type=('build'))
    depends_on('autoconf', when='@main', type=('build'))
    depends_on('automake', when='@main', type=('build'))
    depends_on('libtool', when='@main', type=('build'))
