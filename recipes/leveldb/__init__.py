from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class LevelDBRecipe(Recipe):
    version = '1.18'
    url = 'https://github.com/google/leveldb/archive/v{version}.tar.gz'
    opt_depends = ['snappy']

    def should_build(self, arch):
        return not ( self.has_libs(arch, 'libleveldb.so') )
                   # and self.ctx.has_package('libtorrent.so', arch.arch) )

    def build_arch(self, arch):
        super(LevelDBRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Make sure leveldb is compiled for Android and does not include versioned numbers
            env['TARGET_OS'] = 'OS_ANDROID_CROSSCOMPILE'
            #FIXME: Not idempotent
            shprint(sh.sed, '-i', '127i\ \ \ \ \ \ \ \ PLATFORM_SHARED_VERSIONED=', 'build_detect_platform')
            # Build
            shprint(sh.make, _env=env)
            # Copy the shared library
            shutil.copyfile('libleveldb.so', join(self.ctx.get_libs_dir(arch.arch), 'libleveldb.so'))

    def get_recipe_env(self, arch):
        env = super(LevelDBRecipe, self).get_recipe_env(arch)
        #env['PYTHON_ROOT'] = self.ctx.get_python_install_dir()
        env['CFLAGS'] += ' -I' + self.ctx.ndk_dir + '/platforms/android-' + str(self.ctx.android_api) + '/arch-' + arch.arch.replace('eabi', '') + '/usr/include' + \
                         ' -I' + self.ctx.ndk_dir + '/sources/cxx-stl/gnu-libstdc++/' + self.ctx.toolchain_version + '/include' + \
                         ' -I' + self.ctx.ndk_dir + '/sources/cxx-stl/gnu-libstdc++/' + self.ctx.toolchain_version + '/libs/' + arch.arch + '/include'
                         #' -I' + env['PYTHON_ROOT'] + '/include/python2.7'
        env['CXXFLAGS'] = env['CFLAGS']
        env['CXXFLAGS'] += ' -frtti'
        env['CXXFLAGS'] += ' -fexceptions'
        env['LDSHARED'] = env['CC']
        env['LDFLAGS'] += ' -L' + self.ctx.ndk_dir + '/sources/cxx-stl/gnu-libstdc++/' + self.ctx.toolchain_version + '/libs/' + arch.arch + \
                          ' -lgnustl_shared'
                          #' -L' + env['PYTHON_ROOT'] + '/lib' + \
                          #' -lpython2.7'
        return env

recipe = LevelDBRecipe()
