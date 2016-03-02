from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class PyLevelDBRecipe(PythonRecipe):
    version = '0.193'
    url = 'https://pypi.python.org/packages/source/l/leveldb/leveldb-{version}.tar.gz'
    depends = ['leveldb', 'hostpython2', 'python2', 'setuptools']
    call_hostpython_via_targetpython = False
    patches = ['bindings-only.patch']

    def should_build(self, arch):
        return not self.ctx.has_package('leveldb', arch.arch)

    def build_arch(self, arch):
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Overwrite with source from leveldb recipe
            sh.cp('-rf', self.get_recipe('leveldb', self.ctx).get_build_dir(arch.arch),
                         self.get_build_dir(arch.arch))
            # Remove snappy source in this pypi package
            sh.rm('-rf', './snappy')
            if 'snappy' in recipe.ctx.recipe_build_order:
                # Use source from snappy recipe
                sh.ln('-s', self.get_recipe('snappy', self.ctx).get_build_dir(arch.arch), 'snappy')
            # Build python bindings
            hostpython = sh.Command(self.hostpython_location)
            shprint(hostpython,
                    'setup.py',
                    'build'
            , _env=env)
        # Install python bindings
        super(PyLevelDBRecipe, self).build_arch(arch)

    def get_recipe_env(self, arch):
        env = super(PyLevelDBRecipe, self).get_recipe_env(arch)
        # Copy environment from leveldb recipe
        env.update(self.get_recipe('leveldb', self.ctx).get_recipe_env(arch))
        env['PYTHON_ROOT'] = self.ctx.get_python_install_dir()
        env['CFLAGS'] += ' -I' + env['PYTHON_ROOT'] + '/include/python2.7'
        # Set linker to use the correct gcc
        env['LDSHARED'] = env['CC'] + ' -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions'
        env['LDFLAGS'] += ' -L' + env['PYTHON_ROOT'] + '/lib' + \
                          ' -lpython2.7' + \
                          ' -lleveldb'
        return env

recipe = PyLevelDBRecipe()
