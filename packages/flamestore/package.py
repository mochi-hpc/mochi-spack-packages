##############################################################################
#
# Installing flamestore:
#
#     spack install flamestore
#
from spack import *


class Flamestore(PythonPackage):
    """Transient distributed object store for deep learning"""

    homepage = "https://xgitlab.cels.anl.gov/sds/flame-store"
    url      = "https://xgitlab.cels.anl.gov/sds/flame-store.git"

    version('master',  git="https://xgitlab.cels.anl.gov/sds/flame-store.git")

    depends_on('py-margo')
    depends_on('py-bake+numpy')
    depends_on('py-h5py')
    depends_on('py-keras')
    depends_on('py-mpi4py')
