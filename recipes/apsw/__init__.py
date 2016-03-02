from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class ApswRecipe(PythonRecipe):
    version = '3.11.0-r1'
    url = 'https://github.com/rogerbinns/apsw/archive/{version}.tar.gz'
    depends = ['sqlite3', 'hostpython2', 'python2', 'setuptools']
    call_hostpython_via_targetpython = False
    site_packages_name = 'apsw'

    def build_arch(self, arch):
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Build python bindings
            hostpython = sh.Command(self.hostpython_location)
            shprint(hostpython,
                    'setup.py',
                    'build',
                    '--enable=fts4'
            , _env=env)
        # Install python bindings
        super(ApswRecipe, self).build_arch(arch)

    def get_recipe_env(self, arch):
        env = super(ApswRecipe, self).get_recipe_env(arch)
        env['CFLAGS'] += ' -I' + self.get_recipe('sqlite3', self.ctx).get_build_dir(arch.arch)
        env['LDFLAGS'] += ' -lsqlite3'
        return env

recipe = ApswRecipe()
