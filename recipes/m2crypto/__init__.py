from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class M2CryptoRecipe(Recipe):
    version = '0.23.0'
    url = 'https://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-{version}.tar.gz'
    #md5sum = '89557730e245294a6cab06de8ad4fb42'
    depends = ['openssl', 'hostpython2', 'python2']

    def build_arch(self, arch):
        super(M2CryptoRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            hostpython = sh.Command(join(env['HOSTPYTHON_BUILD_PATH'], 'hostpython'))
            # Build M2Crypto
            shprint(hostpython,
                    'setup.py',
                    'build_ext',
                    '--openssl=' + env['OPENSSL_BUILD_PATH'],
                    '--library-dirs=' + env['OPENSSL_BUILD_PATH']
            , _env=env)
            # Install M2Crypto
            shprint(hostpython,
                    'setup.py',
                    'install',
                    '-O2',
                    '--prefix ' + self.ctx.get_python_install_dir()
            , _env=env)

    def get_recipe_env(self, arch):
        env = super(M2CryptoRecipe, self).get_recipe_env(arch)
        env['HOSTPYTHON_BUILD_PATH'] = self.get_recipe('hostpython2', self.ctx).get_build_dir(arch.arch)
        env['OPENSSL_BUILD_PATH'] = self.get_recipe('openssl', self.ctx).get_build_dir(arch.arch)
        env['CFLAGS'] += ' -I' + join(self.ctx.get_python_install_dir(), 'include/python2.7')
        env['PYTHONPATH'] = self.ctx.get_site_packages_dir(arch.arch)
        return env

recipe = M2CryptoRecipe()
