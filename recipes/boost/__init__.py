from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import exists, join
import sh

# This recipe only downloads Boost and builds Boost.Build
# Since Boost by default uses version numbers in the library names, it makes linking to them harder (as Android does not accept version numbers)
# This is used in the libtorrent recipe and Boost.Build is used to (recursivly) compile Boost from the source here
class BoostRecipe(Recipe):
    version = '1.58.0'
    # Don't forget to change the URL when changing the version
    url = 'http://downloads.sourceforge.net/project/boost/boost/{version}/boost_1_58_0.tar.bz2'
    depends = ['python2']

    def prebuild_arch(self, arch):
        super(BoostRecipe, self).prebuild_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            # Export the Boost location to other recipes that want to know where to find Boost
            env['BOOST_ROOT'] = self.get_build_dir(arch.arch)
            # Export PYTHON_INSTALL as it is used in user-config
            env['PYTHON_INSTALL'] = join(self.get_recipe('python2', self.ctx).get_build_dir(arch.arch), 'python-install')
            # Export hostpython
            env['HOSTPYTHON'] = join(self.get_recipe('hostpython2', self.ctx).get_build_dir(arch.arch), 'hostpython')

            # Make Boost.Build
            bash = sh.Command('bash')
            shprint(bash, 'bootstrap.sh',
                    '--with-python=' + env['HOSTPYTHON'],
                    '--with-python-root=' + env['PYTHON_INSTALL'],
                    '--with-python-version=2.7',
                    _env=env)

            # Overwrite the user-config
            recipe_config = join(self.get_recipe_dir(), 'user-config.jam')
            boost_config = join(self.get_build_dir(arch.arch), 'tools/build/src/user-config.jam')
            shutil.copyfile(recipe_config, boost_config)

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
            # Copy libgnustl
            lib = join(self.ctx.ndk_dir, 'sources/cxx-stl/gnu-libstdc++', env['TOOLCHAIN_VERSION'], 'libs', arch.arch, 'libgnustl_shared.so')
            shprint(sh.cp, lib, self.ctx.get_libs_dir(arch.arch))

recipe = BoostRecipe()