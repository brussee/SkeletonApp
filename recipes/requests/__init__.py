from pythonforandroid.toolchain import PythonRecipe

class RequestsRecipe(PythonRecipe):
    version = '2.9.1'
    url = 'https://pypi.python.org/packages/source/r/requests/requests-{version}.tar.gz'
    #md5sum = '0b7f480d19012ec52bab78292efd976d'
    depends = ['hostpython2']
    site_packages_name = 'requests'

recipe = RequestsRecipe()
