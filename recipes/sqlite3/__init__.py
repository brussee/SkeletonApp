from pythonforandroid.toolchain import NDKRecipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class Sqlite3Recipe(NDKRecipe):
    version = '3.12.1'
    # Don't forget to change the URL when changing the version
    url = 'https://www.sqlite.org/2016/sqlite-amalgamation-3120100.zip'
    generated_libraries = ['sqlite3']

    def should_build(self, arch):
        return not self.has_libs(arch, 'libsqlite3.so')

    def prebuild_arch(self, arch):
        super(Sqlite3Recipe, self).prebuild_arch(arch)
        sh.mkdir('-p', join(self.get_build_dir(arch.arch), 'jni'))

    def build_arch(self, arch, *extra_args):
        shutil.copyfile(join(self.get_recipe_dir(), 'Android-static.mk'),
                        join(self.get_build_dir(arch.arch), 'jni/Android.mk'))
        # Build static lib
        super(Sqlite3Recipe, self).build_arch(arch)
        shutil.copyfile(join(self.get_build_dir(arch.arch), 'obj/local', arch.arch, 'libsqlite3.a'),
                        join(self.ctx.get_libs_dir(arch.arch), 'libsqlite3.a'))

        shutil.copyfile(join(self.get_recipe_dir(), 'Android-shared.mk'),
                        join(self.get_build_dir(arch.arch), 'jni/Android.mk'))
        # Build shared lib
        super(Sqlite3Recipe, self).build_arch(arch)
        shutil.copyfile(join(self.get_build_dir(arch.arch), 'libs', arch.arch, 'libsqlite3.so'),
                        join(self.ctx.get_libs_dir(arch.arch), 'libsqlite3.so'))

    def get_recipe_env(self, arch):
        env = super(Sqlite3Recipe, self).get_recipe_env(arch)
        env['NDK_PROJECT_PATH'] = self.get_build_dir(arch.arch)
        return env

recipe = Sqlite3Recipe()
