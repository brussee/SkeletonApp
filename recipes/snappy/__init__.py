from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class SnappyRecipe(Recipe):
    version = '1.1.3'
    url = 'https://github.com/google/snappy/releases/download/{version}/snappy-{version}.tar.gz'

    def should_build(self, arch):
        # Only download to use in leveldb recipe
        return not 'leveldb' in recipe.ctx.recipe_build_order

    def build_arch(self, arch):
        super(SnappyRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Configure
            bash = sh.Command('bash')
            shprint(bash, 'configure',
                    '--host=' + self.select_build_arch(arch),
            _env=env)
            # Build
            shprint(sh.make, _env=env)
            # Install
            shprint(sh.make, 'install', _env=env)

    def select_build_arch(self, arch):
        return arch.arch.replace('eabi', '')

recipe = SnappyRecipe()
