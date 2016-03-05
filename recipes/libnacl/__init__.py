from pythonforandroid.toolchain import PythonRecipe

class LibNaClRecipe(PythonRecipe):
    version = '1.4.4'
    url = 'https://pypi.python.org/packages/source/l/libnacl/libnacl-{version}.tar.gz'
    #md5sum = '797154ac51b9ca4c6cf4b2e6eff73e25'
    depends = ['hostpython2', 'setuptools']
    site_packages_name = 'libnacl'

recipe = LibNaClRecipe()
