# spack-packages for the Mercury Suite

Here are a collection of [spack](https://spack.io/)  packages to manage
building the Mercury Suite.

For more about spack and what you can do with it, spack has lots of
[documentation](https://spack.readthedocs.io/en/latest/) and a good
[tutorial](https://spack.readthedocs.io/en/latest/tutorial_sc16.html).

## Installation

Once you've set up spack itself, you need to teach it about this collection
('repository' in spack lingo) of pacakges.  Go to the top-level directory of
this project and execute the following command:

    spack repo add .

Did it work?

    spack repo list
