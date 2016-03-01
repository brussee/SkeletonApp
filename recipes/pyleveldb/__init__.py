from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class PyLevelDBRecipe(PythonRecipe):
    version = '0.193'
    url = 'https://pypi.python.org/packages/source/l/leveldb/leveldb-{version}.tar.gz'
    #md5sum = '2952434f2a0ce10c44f58542cc561589'
    depends = ['leveldb', 'hostpython2', 'python2', 'setuptools']
    call_hostpython_via_targetpython = False

    def should_build(self, arch):
        return not self.ctx.has_package('leveldb', arch.arch)

    def build_arch(self, arch):
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Copy latest version from leveldb recipe
            sh.cp('-rf', self.get_recipe('leveldb', self.ctx).get_build_dir(arch.arch),
                         self.get_build_dir(arch.arch))
            # Overwrite configuration
            #TODO make patch file
            shutil.copyfile(join(self.get_recipe_dir(), 'setup.py'),
                            join(self.get_build_dir(arch.arch), 'setup.py'))
            # Build LevelDB python bindings
            hostpython = sh.Command(self.hostpython_location)
            shprint(hostpython,
                    'setup.py',
                    'build'
            , _env=env)
        # Install LevelDB python bindings
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
