from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import join, exists
import sh


class FFMpegRecipe(Recipe):

    patches = ['settings.patch']


    def should_build(self, arch):
        build_dir = self.get_build_dir(arch.arch)
        return not exists(join(build_dir, 'build', self.select_build_arch(arch), 'bin', 'ffmpeg'))


    def prebuild_arch(self, arch):
        super(FFMpegRecipe, self).prebuild_arch(arch)
        build_dir = self.get_build_dir(arch.arch)
        bash = sh.Command('bash')
        git = sh.Command('git')
        # Clone master branch
        if not exists(build_dir):
            shprint(git, 'clone', 'https://github.com/WritingMinds/ffmpeg-android', build_dir)
            # Download submodules
            with current_directory(build_dir):
                shprint(bash, 'init_update_libs.sh')
        else:
            shprint(git, 'pull')
            shprint(git, 'submodule', 'update')


    def build_arch(self, arch):
        super(FFMpegRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        build_dir = self.get_build_dir(arch.arch)
        with current_directory(build_dir):
            bash = sh.Command('bash')
            shprint(bash, 'android_build.sh', _env=env)


    def select_build_arch(self, arch):
        return arch.arch.replace('armeabi', 'armeabi-v7a')


    def get_recipe_env(self, arch):
        env = super(FFMpegRecipe, self).get_recipe_env(arch)
        env['ANDROID_NDK'] = self.ctx.ndk_dir
        env['ANDROID_API'] = str(self.ctx.android_api)
        return env


recipe = FFMpegRecipe()