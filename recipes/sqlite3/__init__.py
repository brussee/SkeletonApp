from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class Sqlite3Recipe(Recipe):
    version = '3.11.1'
    # Don't forget to change the URL when changing the version
    url = 'https://www.sqlite.org/2016/sqlite-autoconf-3110100.tar.gz'
    generated_libraries = ['sqlite3']

    def should_build(self, arch):
        return not self.has_libs(arch, 'libsqlite3.so')

    def prebuild_arch(self, arch):
        super(Sqlite3Recipe, self).prebuild_arch(arch)
        # Copy the Android make file
        #sh.mkdir('-p', join(self.get_build_dir(arch.arch), 'jni'))
        #shutil.copyfile(join(self.get_recipe_dir(), 'Android.mk'),
        #                join(self.get_build_dir(arch.arch), 'jni/Android.mk'))

    def select_build_arch(self, arch):
        return arch.arch.replace('eabi', '')

    def build_arch(self, arch, *extra_args):
        super(Sqlite3Recipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Configure
            bash = sh.Command('bash')
            shprint(bash, './configure',
                    '--host=' + self.select_build_arch(arch),
                    '--prefix=' + self.get_build_dir(arch.arch),
                    '--exec_prefix=' + self.get_build_dir(arch.arch),
                    '--enable-shared=' + 'yes',
                    '--enable-static=' + 'no',
                    '--enable-threadsafe=' + 'yes',
                    '--enable-dynamic-extensions=' + 'yes',
                    '--enable-fts5=' + 'no',
                    '--enable-json1=' + 'no',
                    '--enable-static-shell=' + 'no'
            , _env=env)
            # Make
            make = sh.Command('make')
            shprint(make, 'install', 'sqlite3.c')

        # Copy the shared library
        #shutil.copyfile(join(self.get_build_dir(arch.arch), 'libs', arch.arch, 'libsqlite3.so'),
        #                join(self.ctx.get_libs_dir(arch.arch), 'libsqlite3.so'))

    def get_recipe_env(self, arch):
        env = super(Sqlite3Recipe, self).get_recipe_env(arch)
        #env['NDK_PROJECT_PATH'] = self.get_build_dir(arch.arch)
        return env

recipe = Sqlite3Recipe()
