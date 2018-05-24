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
    version('mochi', git="https://xgitlab.cels.anl.gov/sds/flame-store.git",
            branch='dev-mochi-backend', preferred=True)

    depends_on('py-margo')
    depends_on('py-sdskv')
    depends_on('py-bake+numpy')
    depends_on('py-h5py')
    depends_on('py-keras')
    depends_on('py-mpi4py')
