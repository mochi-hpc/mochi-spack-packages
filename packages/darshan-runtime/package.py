
from spack.pkg.builtin.darshan_runtime import DarshanRuntime as BuiltinDarshanRuntime


class DarshanRuntime(BuiltinDarshanRuntime):

    variant('hdf5', default=False, description='additional HDF5 statistics')

    depends_on('hdf5@1.10.0:', when='+hdf5')

    def configure_args(self):
        spec = self.spec
        config_args = super(DarshanRuntime, self).configure_args()

        if '+hdf5' in spec:
            config_args.append('--enable-hdf5-mod')

        return config_args
