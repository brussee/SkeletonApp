from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class PyAVRecipe(PythonRecipe):

    version = 'master'
    url = 'https://github.com/mikeboers/PyAV/archive/{version}.zip'
    depends = ['ffmpeg', 'python2', 'setuptools']
    call_hostpython_via_targetpython = False
    site_packages_name = 'av'


    def build_arch(self, arch):
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Build python bindings
            hostpython = sh.Command(self.hostpython_location)
            shprint(hostpython,
                    'setup.py',
                    'build_ext',
                    '--ffmpeg-dir=' + join(self.get_recipe('ffmpeg', self.ctx).get_build_dir(arch.arch), 'build', self.select_build_arch(arch))
            , _env=env)
        # Install python bindings
        super(PyAVRecipe, self).build_arch(arch)


    def select_build_arch(self, arch):
        return arch.arch.replace('armeabi', 'armeabi-v7a')


recipe = PyAVRecipe()