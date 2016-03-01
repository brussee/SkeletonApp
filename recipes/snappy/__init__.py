from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class SnappyRecipe(Recipe):
    version = '1.1.3'
    url = 'https://github.com/google/snappy/releases/download/{version}/snappy-{version}.tar.gz'

    def should_build(self, arch):
        return not self.has_libs(arch, 'libsnappy.so')

    def build_arch(self, arch):
        super(SnappyRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Build
            shprint(sh.make, _env=env)

    def get_recipe_env(self, arch):
        env = super(SnappyRecipe, self).get_recipe_env(arch)
        return env

recipe = SnappyRecipe()
