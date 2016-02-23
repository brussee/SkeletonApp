from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class M2CryptoRecipe(PythonRecipe):
    version = '0.23.0'
    url = 'https://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-{version}.tar.gz'
    #md5sum = '89557730e245294a6cab06de8ad4fb42'
    depends = ['openssl', 'hostpython2', 'python2', 'setuptools']
    site_packages_name = 'm2crypto'
    call_hostpython_via_targetpython = False

    def build_arch(self, arch):
        # Override super
        super(PythonRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            hostpython = sh.Command(self.hostpython_location)
            # Build M2Crypto
            shprint(hostpython,
                    'setup.py',
                    'build_ext',
                    '--openssl=' + env['OPENSSL_BUILD_PATH'],
                    '--library-dirs=' + env['OPENSSL_BUILD_PATH']
            , _env=env)
        self.install_python_package(arch)

    def get_recipe_env(self, arch):
        env = super(M2CryptoRecipe, self).get_recipe_env(arch)
        env['OPENSSL_BUILD_PATH'] = self.get_recipe('openssl', self.ctx).get_build_dir(arch.arch)
        env['CFLAGS'] += ' -I' + join(self.ctx.get_python_install_dir(), 'include/python2.7')
        return env

recipe = M2CryptoRecipe()
