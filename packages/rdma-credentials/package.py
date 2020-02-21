# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
from spack import *


# in order to use this package you will need to load the modules. In
# packages.yaml add a stanza like this:
#
#    rdma-credentials:
#        modules:
#            rdma-credentials@1.2.21: rdma-credentials/1.2.21-6.0.7.1_8.6__gbd83ea9.ari
#        buildable: False

class RdmaCredentials(Package):
    """Dynamic RDMA Credentials (DRC) is a Cray XC system service that enables
    shared network access between different user applications. DRC enables user
    applications to request managed network credentials, which can be shared
    with other users, groups, or jobs. Access to a credential is governed by
    the application and DRC to provide authorized and protected sharing of
    network access between applications. DRC extends the existing protection
    domain functionality provided by ALPS without exposing application data to
    unauthorized applications. DRC can also be used with other batch systems,
    such as Slurm, without any loss of functionality."""

    homepage = "https://pubs.cray.com/content/S-2587/CLE%206.0.UP04/xctm-series-dynamic-rdma-credentials-best-practices-guide-cle60up04-s-2587/about-the-xc-series-dynamic-rdma-credentials-best-practices-guide-s-2587"


    def install(self, spec, prefix):
        raise InstallError('Cray rdma-credentials is not installable; it is vendor supplied')
