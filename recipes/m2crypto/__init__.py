from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class M2CryptoRecipe(Recipe):
    version = '0.23.0'
    url = 'https://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-{version}.tar.gz'
    md5sum = '89557730e245294a6cab06de8ad4fb42'
    depends = ['openssl', 'hostpython', 'python2']

    def build_arch(self, arch):
        super(M2CryptoRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            bash = sh.Command('bash')

    def get_recipe_env(self, arch):
        env = super(M2CryptoRecipe, self).get_recipe_env(arch)
        env['OPENSSL_BUILD_PATH'] = self.get_recipe('openssl', self.ctx).get_build_dir()
        return env

recipe = M2CryptoRecipe()
