from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import exists, join
import sh

# This recipe only downloads Boost and builds Boost.Build
# Since Boost by default uses version numbers in the library names, it makes linking to them harder (as Android does not accept version numbers)
# This is used in the libtorrent recipe and Boost.Build is used to (recursivly) compile Boost from the source here
class BoostRecipe(Recipe):
    version = '1.58.0'
    # Don't forget to change the URL when changing the version
    url = 'http://downloads.sourceforge.net/project/boost/boost/{version}/boost_1_58_0.tar.gz'
    depends = ['python2']

    def prebuild_arch(self, arch):
        super(BoostRecipe, self).prebuild_arch(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Make Boost.Build
            bash = sh.Command('bash')
            shprint(bash, 'bootstrap.sh', '--with-python=$HOSTPYTHON', '--with-python-root=$BUILD_PATH/python-install', '--with-python-version=2.7')
            # Overwrite the user-config
            recipe_config = join(self.get_recipe_dir(), 'user-config.jam')
            boost_config = join(self.get_build_dir(arch.arch), 'tools/build/src/user-config.jam')
            shprint(sh.cp, recipe_config, boost_config)
            # Replace the generated project-config with our own
            shprint(sh.rm, '-f', join(self.get_build_dir(arch.arch), 'project-config.jam*'))
            shprint(sh.cp, join(self.get_recipe_dir(), 'project-config.jam'), self.get_build_dir(arch.arch))
            # Create Android case for library linking when building Boost.Python
            #FIXME: Not idempotent
            shprint(sh.sed, '-i', '622i\ \ \ \ \ \ \ \ case * : return ;', 'tools/build/src/tools/python.jam')

    def build_arch(self, arch):
        super(BoostRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            bash = sh.Command('bash')

            # Export the Boost location to other recipes that want to know where to find Boost
            env['BOOST_ROOT']="' + self.get_build_dir(arch.arch) + '"')
            # Export PYTHON_INSTALL as it is used in user-config
            shprint(sh.export, 'PYTHON_INSTALL="$BUILD_PATH/python-install"')

            # Copy libgnustl
            shprint(sh.cp, '$ANDROIDNDK/sources/cxx-stl/gnu-libstdc++/$TOOLCHAIN_VERSION/libs/$ARCH/libgnustl_shared.so', self.ctx.get_libs_dir(arch.arch))

    def postbuild_arch(self, arch):
        super(BoostRecipe, self).postbuild_arch(arch)
        shprint(sh.unset, 'BOOST_ROOT')
        shprint(sh.unset, 'PYTHON_INSTALL')

recipe = BoostRecipe()
