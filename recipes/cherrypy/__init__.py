from pythonforandroid.toolchain import PythonRecipe

class CherryPyRecipe(PythonRecipe):
    version = '5.0.1'
    url = 'https://pypi.python.org/packages/source/C/CherryPy/CherryPy-{version}.tar.gz'
    #md5sum = '4a475ff1e2a580d29aa3ab8bb98268a6'
    depends = ['hostpython2']
    site_packages_name = 'cherrypy'
    call_hostpython_via_targetpython = False

recipe = CherryPyRecipe()
