from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import join
import sh

# This recipe creates a custom toolchain and bootstraps Boost from source to build Boost.Build
# including python bindings
class BoostRecipe(Recipe):
    version = '1.60.0'
    # Don't forget to change the URL when changing the version
    url = 'http://downloads.sourceforge.net/project/boost/boost/{version}/boost_1_60_0.tar.bz2'
    depends = ['python2']

    def should_build(self, arch):
        return not exists(join(self.get_build_dir(arch.arch), 'b2'))

    def prebuild_arch(self, arch):
        super(BoostRecipe, self).prebuild_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Make custom toolchain
            bash = sh.Command('bash')
            shprint(bash, join(self.ctx.ndk_dir, 'build/tools/make-standalone-toolchain.sh'),
                    '--ndk-dir=' + self.ctx.ndk_dir,
                    '--arch=' + env['ARCH'],
                    '--platform=android-' + str(self.ctx.android_api),
                    '--toolchain=' + env['CROSSHOST'] + '-' + env['TOOLCHAIN_VERSION'],
                    '--install-dir=' + env['CROSSHOME'],
                    '--system=' + 'linux-x86_64'
            )

    def build_arch(self, arch):
        super(BoostRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Compile Boost.Build engine with this custom toolchain
            bash = sh.Command('bash')
            shprint(bash, 'bootstrap.sh',
                    '--with-python=' + join(env['PYTHON_ROOT'], 'bin/python.host'),
                    '--with-python-version=2.7',
                    '--with-python-root=' + env['PYTHON_ROOT']
            )  # Do not pass env
            shutil.copyfile(join(self.get_recipe_dir(), 'user-config.jam'),
                            join(env['BOOST_BUILD_PATH'], 'user-config.jam'))
            # Disable version suffix of shared object files
            self.apply_patch(join(self.get_recipe_dir(), 'disable-so-version.patch'), arch.arch)
            # Create Android case for library linking when building Boost.Python
            self.apply_patch(join(self.get_recipe_dir(), 'use-android-libs.patch'), arch.arch)

    def select_build_arch(self, arch):
        return arch.arch.replace('eabi', '')

    def get_recipe_env(self, arch):
        env = super(BoostRecipe, self).get_recipe_env(arch)
        #env['OPENSSL_BUILD_PATH'] = self.get_recipe('openssl', self.ctx).get_build_dir(arch.arch)
        env['BOOST_BUILD_PATH'] = self.get_build_dir(arch.arch)  # find user-config.jam
        env['BOOST_ROOT'] = env['BOOST_BUILD_PATH']  # find boost source
        env['PYTHON_ROOT'] = self.ctx.get_python_install_dir()
        env['ARCH'] = self.select_build_arch(arch)
        env['ANDROIDAPI'] = str(self.ctx.android_api)
        env['CROSSHOST'] = env['ARCH'] + '-linux-androideabi'
        env['CROSSHOME'] = join(env['BOOST_ROOT'], 'standalone-' + env['ARCH'] + '-toolchain')
        env['TOOLCHAIN_PREFIX'] = join(env['CROSSHOME'], 'bin', env['CROSSHOST'])
        return env

recipe = BoostRecipe()
