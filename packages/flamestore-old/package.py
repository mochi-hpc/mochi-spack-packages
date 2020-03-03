##############################################################################
#
# Installing flamestore:
#
#     spack install flamestore
#
from spack import *


class FlamestoreOld(PythonPackage):
    """Transient distributed object store for deep learning"""

    homepage = "https://xgitlab.cels.anl.gov/sds/flame-store-old"
    url      = "https://xgitlab.cels.anl.gov/sds/flame-store-old"
    git      = "https://xgitlab.cels.anl.gov/sds/flame-store-old.git"

    version('develop', branch='master')
    version('0.1', tag='v0.1')

    depends_on('py-mochi-margo@0.1:')
    depends_on('py-mochi-bake+numpy@0.1:')
    depends_on('py-h5py')
    depends_on('py-keras')
    depends_on('py-mpi4py')
