from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import exists, join
import sh

# This recipe only downloads Boost and builds Boost.Build
# Since Boost by default uses version numbers in the library names, it makes linking to them harder (as Android does not accept version numbers)
# This is used in the libtorrent recipe and Boost.Build is used to (recursivly) compile Boost from the source here
class BoostRecipe(Recipe):
    version = '1.60.0'
    # Don't forget to change the URL when changing the version
    url = 'http://downloads.sourceforge.net/project/boost/boost/{version}/boost_1_60_0.tar.bz2'
    depends = ['python2']

    def prebuild_arch(self, arch):
        super(BoostRecipe, self).prebuild_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # make custom toolchain
            bash = sh.Command('bash')
            shprint(bash, join(self.ctx.ndk_dir, 'build/tools/make-standalone-toolchain.sh'),
                    '--ndk-dir=' + self.ctx.ndk_dir,
                    '--arch=' + arch.arch,
                    '--platform=android-' + str(self.ctx.android_api),
                    '--toolchain=' + env['CROSSHOST'] + '-' + env['TOOLCHAIN_VERSION'],
                    '--install-dir=' + env['CROSSHOME'],
                    '--system=' + 'linux-x86_64'
            )

    def build_arch(self, arch):
        super(BoostRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # compile Boost.Build engine with this custom toolchain
            shprint(sh.cd, env['BOOST_ROOT'])
            bash = sh.Command('bash')
            shprint(bash, 'bootstrap.sh'
            #        '--with-python=python.host', #join(env['PYTHON_ROOT'], 'bin', 'python.host')
            #        '--with-python-version=2.7',
            #        '--with-python-root=' + env['PYTHON_ROOT']
            )  # do not pass env!

            shprint(sh.cp, '/home/brussee/repos/SkeletonApp/recipes/boost/user-config.jam', '/home/brussee')

    def get_recipe_env(self, arch):
        env = super(BoostRecipe, self).get_recipe_env(arch)
        env['CROSSHOST'] = arch.arch + '-linux-androideabi'
        env['CROSSHOME'] = '/home/brussee/custom-' + arch.arch + '-toolchain'
        env['BOOST_ROOT'] = '/home/brussee/boost_1_60_0'
        env['PYTHON_ROOT'] = self.ctx.get_python_install_dir()
        print(env)
        return env

recipe = BoostRecipe()