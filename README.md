# spack-packages for the Mercury Suite

Here are a collection of [spack](https://spack.io/)  packages to manage
building the Mercury Suite.

For more about spack and what you can do with it, spack has lots of
[documentation](https://spack.readthedocs.io/en/latest/) and a good
[tutorial](https://spack.readthedocs.io/en/latest/tutorial_sc16.html).

## Repo Installation

Once you've set up spack itself (you added `spack` to your `$PATH`, right?),
 you need to teach it about this collection
('repository' in spack lingo) of packages.  Go to the top-level directory of
this project and execute the following command:

    cd sds-repo
    spack repo add .

Did it work?

    spack repo list

## Mochi Suite Installation

To build the entire mochi suite with the default configuration (mercury using
CCI's TCP transport), simply build margo:

    spack install margo


### Side note: System packages vs spack packages

The largest dependency for Mercury is the Boost package.  If your system
already has Boost, you can teach spack about it and other
[system packages](https://spack.readthedocs.io/en/latest/getting_started.html#system-packages).

Let's say you installed Boost through your distribution (an RPM or DEB package)
To inform spack about Boost you e.g. installed from an RPM, you would add it to
`~/.spack/<arch>/packages.yaml`

```
packages:
    boost:
        paths:
            boost@system: /usr
        version: [system]
        buildable: False
```

I have found several other large dependencies that are handled just fine by the
operating system.  My `${HOME}/.spack/linux/packages.yaml` file looks like
this:

```
packages:
    openssl:
        paths:
            openssl@1.0.2g: /usr
        buildable: False
    cmake:
        paths:
            cmake@3.9.1: /usr
        buildable: False
    boost:
        paths:
            boost@1.62: /usr
        buildable: False
    autoconf:
        paths:
            autoconf@2.69: /usr
        buildable: False
    automake:
        paths:
            automake@1.15.1: /usr
        buildable: False
    mpich:
        paths:
            mpich@master: /home/robl/work/soft/mpich
        buildable: False
```

You can see that I have flagged several packages as `buildable: False`,
generaly because they are either large packages or have large dependencies.  I
tend to work from MPICH's latest version in git, so I have also told spack
about my locally installed MPICH.

These `packages` files live in a platform-specific directory (run `spack arch
-p` to see what platform spack thinks you are on).  Pretty helpful for e.g.
Argonne, where a home file system is shared between a linux cluster, a blue
gene, and a Cray.  You can describe `packages.py` for each platform.

## Using Mochi Suite

One consequence of the spack design (where packages are installed into a prefix
based on a hash of their configuration and compiler) is that library and header
paths are unwieldy.  An environment-management tool such as `modules` helps a
lot here, and is nicely integrated into spack:

```
 module avail

 --- /blues/gpfs/home/robl/src/spack/share/spack/modules/linux-centos6-x86_64 ---
 abtsnoozer-master-gcc-4.7.2-4ygmjep libev-4.24-gcc-4.7.2-ddpazlc
 argobots-master-gcc-4.7.2-4wxy6p3   libsigsegv-2.10-gcc-4.7.2-vtvikjs
 autoconf-2.69-gcc-4.7.2-a2clqmr     libtool-2.4.6-gcc-4.7.2-nxthahu
 automake-1.15-gcc-4.7.2-bfjmuzz     m4-1.4.18-gcc-4.7.2-hftmdfw
 boost-1.63.0-gcc-4.7.2-ds3fbl3      margo-master-gcc-4.7.2-uy4in2w
 bzip2-1.0.6-gcc-4.7.2-jehobzs       mercury-master-gcc-4.7.2-eiyjtqs
 cci-2.0-gcc-4.7.2-5y6vgzq           zlib-1.2.10-gcc-4.7.2-w53w2nl
 ...
```

Load the margo module into your environment:

    module add margo-master-gcc-4.7.2-uy4in2w

Spack integrages with modules: the integration helps with managing spack's hash-oriented naming convention

    spack load margo

The integration can also help you load in all the dependencies:

    source <(spack module loads  --dependencies margo)

sometimes I get `Error: this command needs exactly **one** module type active`: pass 	`-m tcl` like this

    source <(spack module loads  -m tcl --dependencies margo)

```
 module list
Currently Loaded Modulefiles:
  1) margo-master-gcc-4.7.2-uy4in2w
  2) mercury-master-gcc-4.7.2-eiyjtqs
  3) abtsnoozer-master-gcc-4.7.2-4ygmjep
  4) argobots-master-gcc-4.7.2-4wxy6p3
```

The modules framework will update the `PKG_CONFIG_PATH` for you (slightly reformatted to wrap the long lines)

```
 pkg-config --cflags margo
 -I/blues/gpfs/home/robl/src/spack/opt/spack/linux-centos6-x86_64/gcc-4.7.2/argobots-master-4wxy6p3thpyhwgo67t6icducpy3ik6y5/include \
 	-I/blues/gpfs/home/robl/src/spack/opt/spack/linux-centos6-x86_64/gcc-4.7.2/abtsnoozer-master-4ygmjeptxkfddgojrupre624olf2w6mq/include \
	-I/blues/gpfs/home/robl/src/spack/opt/spack/linux-centos6-x86_64/gcc-4.7.2/mercury-master-eiyjtqsdv6yynaylgtm5g7jib7fvnshh/include \
	-I/blues/gpfs/home/robl/src/spack/opt/spack/linux-centos6-x86_64/gcc-4.7.2/boost-1.63.0-ds3fbl3vdsk6u5soirxcdoe3e6dw3iwx/include \
	-I/blues/gpfs/home/robl/src/spack/opt/spack/linux-centos6-x86_64/gcc-4.7.2/cci-2.0-5y6vgzqccmk7n7vehrrcxl5ogukwv3gh/include \
	-I/blues/gpfs/home/robl/src/spack/opt/spack/linux-centos6-x86_64/gcc-4.7.2/margo-master-uy4in2w6xniwn43iio7h6ko3j6hbxvfr/include
 ```

## Possible issues

If you encounter a problem in the build log about `possibly undefined macro:
AM_DISABLE_STATIC`, it's possible the package is using system's (possibly
older) `libtool` and not spack's `libtool`.  I could only resolve this by
loading spack's libtool module: (precise name quite likely to be different on
your system)

    $ module load libtool-2.4.6-gcc-4.7.2-nxthahu

