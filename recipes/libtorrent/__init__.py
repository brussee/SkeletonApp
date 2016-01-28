from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import join
import sh

# This recipe builds libtorrent with Python bindings
# It depends on Boost.Build and the source of several Boost libraries present in BOOST_ROOT,
# which is all provided by the boost recipe
class LibtorrentRecipe(Recipe):
    version = '1.0.8'
    # Don't forget to change the URL when changing the version
    url = 'http://github.com/arvidn/libtorrent/archive/libtorrent-1_0_8.tar.gz'
    depends = ['boost', 'python2']

    def build_arch(self, arch):
        super(LibtorrentRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(join(self.get_build_dir(arch.arch), 'bindings/python')):
            # Compile libtorrent with boost libraries and python bindings
            b2 = sh.Command(join(env['BOOST_ROOT'], 'b2'))
            shprint(b2,
                    '-q',
                    'toolset=gcc-' + env['ARCH'],
                    'target-os=android',
                    'threading=multi',
                    'link=shared',
                    'boost-link=shared',
                    'boost=source',
                    '--prefix=' + env['CROSSHOME'],
                    'release'
            , _env=env)
        # Copy the shared libraries into the libs folder
        build_subdirs = 'gcc-arm/release/boost-link-shared/boost-source/libtorrent-python-pic-on/target-os-android/threading-multi/visibility-hidden'
        boost_version = self.get_recipe('boost', self.ctx).version
        shutil.copyfile(join(env['BOOST_BUILD_PATH'], 'bin.v2/libs/python/build', build_subdirs, 'libboost_python.so.' + boost_version),
                        join(self.ctx.get_libs_dir(arch.arch), 'libboost_python.so.' + boost_version))
        shutil.copyfile(join(env['BOOST_BUILD_PATH'], 'bin.v2/libs/system/build', build_subdirs, 'libboost_system.so.' + boost_version),
                        join(self.ctx.get_libs_dir(arch.arch), 'libboost_system.so.' + boost_version))
        shutil.copyfile(join(self.get_build_dir(arch.arch), 'bin', build_subdirs, 'libtorrent.so.' + self.version),
                        join(self.ctx.get_libs_dir(arch.arch), 'libtorrent.so.' + self.version))
        shutil.copyfile(join(self.get_build_dir(arch.arch), 'bindings/python/bin', build_subdirs, 'libtorrent.so'),
                        join(self.ctx.get_libs_dir(arch.arch), 'libtorrent.so'))

    def get_recipe_env(self, arch):
        env = super(LibtorrentRecipe, self).get_recipe_env(arch)
        env['BOOST_BUILD_PATH'] = self.get_recipe('boost', self.ctx).get_build_dir(arch.arch)  # find user-config.jam
        env['BOOST_ROOT'] = env['BOOST_BUILD_PATH']  # find boost source
        env['PYTHON_ROOT'] = self.ctx.get_python_install_dir()
        env['ARCH'] = arch.arch.replace('eabi', '')
        env['ANDROIDAPI'] = str(self.ctx.android_api)
        env['CROSSHOST'] = env['ARCH'] + '-linux-androideabi'
        env['CROSSHOME'] = join(env['BOOST_ROOT'], 'custom-' + env['ARCH'] + '-toolchain')
        env['TOOLCHAIN_PREFIX'] = join(env['CROSSHOME'], 'bin', env['CROSSHOST'])
        return env

recipe = LibtorrentRecipe()