from spack import *


class MochiAll(CMakePackage):
    """Meta package for all Mochi components"""

    homepage = "https://xgitlab.cels.anl.gov/sds/mochi-all"
    git='https://xgitlab.cels.anl.gov/sds/mochi-all.git'

    version('master', branch='master', preferred=True)
    version('develop', branch='master')

    variant('abt-io', default=True, description='Build mochi-abt-io') 
    variant('bake', default=True, description='Build mochi-bake') 
    variant('ch-placement', default=True, description='Build mochi-ch-placement') 
    variant('sdsdkv', default=False, description='Build mochi-sdsdkv') 
    variant('sdskv', default=True, description='Build mochi-sdskv') 
    variant('margo', default=True, description='Build mochi-margo') 
    variant('mdcs', default=True, description='Build mochi-mdcs') 
    variant('poesie', default=True, description='Build mochi-poesie') 
    variant('remi', default=True, description='Build mochi-remi') 
    variant('ssg', default=True, description='Build mochi-ssg') 
    variant('thallium', default=True, description='Build mochi-thallium') 

    depends_on('mochi-abt-io', when='+abt-io')
    depends_on('mochi-bake', when='+bake')
    depends_on('mochi-ch-placement', when='+ch-placement')
    depends_on('mochi-sdsdkv', when='+sdsdkv')
    depends_on('mochi-sdskv', when='+sdskv')
    depends_on('mochi-margo', when='+margo')
    depends_on('mochi-mdcs', when='+mdcs')
    depends_on('mochi-poesie', when='+poesie')
    depends_on('mochi-remi', when='+remi')
    depends_on('mochi-ssg', when='+ssg')
    depends_on('mochi-thallium', when='+thallium')

    depends_on('mochi-abt-io@develop', when='+abt-io @develop')
    depends_on('mochi-bake@develop', when='+bake @develop')
    depends_on('mochi-ch-placement@develop', when='+ch-placement @develop')
    depends_on('mochi-sdsdkv@develop', when='+sdsdkv @develop')
    depends_on('mochi-sdskv@develop', when='+sdskv @develop')
    depends_on('mochi-margo@develop', when='+margo @develop')
    depends_on('mochi-mdcs@develop', when='+mdcs @develop')
    depends_on('mochi-poesie@develop', when='+poesie @develop')
    depends_on('mochi-remi@develop', when='+remi @develop')
    depends_on('mochi-ssg@develop', when='+ssg @develop')
    depends_on('mochi-thallium@develop', when='+thallium @develop')
