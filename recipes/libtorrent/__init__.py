from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import exists, join
import sh

# This recipe builds libtorrent with it's Python bindings
# It depends on Boost.Build and the source of several Boost libraries present in BOOST_ROOT, which is all provided by the boost recipe
class LibtorrentRecipe(Recipe):
    version = '1.0.5'
    url = 'http://kent.dl.sourceforge.net/project/libtorrent/libtorrent/libtorrent-rasterbar-{version}.tar.gz'
    depends = ['boost', 'python2']

    def should_build(self, arch):
        super(LibtorrentRecipe, self).should_build(arch)
        return not exists(join(self.ctx.get_libs_dir(arch.arch), 'libtorrent.so'))

    def build_arch(self, arch):
        super(LibtorrentRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(join(self.get_build_dir(arch.arch), 'bindings/python')):
            # Some flags that belong in user-config, but only seem to work if put here
            linkflags = '--sysroot=' + join(self.ctx.ndk_dir, 'platforms/android-' + str(self.ctx.android_api), 'arch-arm') + \
            ' -L' + join(self.ctx.ndk_dir, 'sources/cxx-stl/gnu-libstdc++', env['TOOLCHAIN_VERSION'], 'libs', arch.arch) + \
            ' -L' + join(self.get_build_dir(arch.arch), 'python-install/lib') + \
            ' -l' + 'python2.7' + ' -l' + 'gnustl_shared'

            printenv = sh.Command('printenv')
            shprint(printenv)
            print(env)

            # Build the Python bindings with Boost.Build and some dependencies recursively (libtorrent, Boost.*)
            # Also link to openssl
            b2 = sh.Command(join(env['BOOST_ROOT'], 'b2'))
            shprint(b2, '-d+2', '-q', 'target-os=android', 'link=static', 'boost-link=static',
                'boost=source', 'threading=multi', 'toolset=gcc-android', 'geoip=off', 'encryption=tommath',
                'linkflags="' + linkflags + '"', 'release', _env=env)

            shutil.copyfile('libtorrent.so', join(self.ctx.get_libs_dir(arch.arch), 'libtorrent.so'))

    def get_recipe_env(self, arch):
        env = super(LibtorrentRecipe, self).get_recipe_env(arch)
        # Export PYTHON_INSTALL as it is used in user-config
        env['PYTHON_INSTALL'] = self.ctx.get_python_install_dir()
        env['BOOST_ROOT'] = self.get_recipe('boost', self.ctx).get_build_dir(arch.arch)
        env['LDFLAGS'] = ''
        return env

recipe = LibtorrentRecipe()