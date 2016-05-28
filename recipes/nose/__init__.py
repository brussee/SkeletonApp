from pythonforandroid.toolchain import PythonRecipe

class NoseRecipe(PythonRecipe):
    version = '1.3.7'
    url = 'https://pypi.python.org/packages/58/a5/0dc93c3ec33f4e281849523a5a913fa1eea9a3068acfa754d44d88107a44/nose-{version}.tar.gz'
    depends = ['hostpython2', 'setuptools', 'unittest']
    site_packages_name = 'nose'
    call_hostpython_via_targetpython = False

recipe = NoseRecipe()
