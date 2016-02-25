from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class M2CryptoRecipe(PythonRecipe):
    version = '0.23.0'
    url = 'https://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-{version}.tar.gz'
    #md5sum = '89557730e245294a6cab06de8ad4fb42'
    depends = ['openssl', 'hostpython2', 'python2', 'setuptools']
    site_packages_name = 'm2crypto'
    call_hostpython_via_targetpython = False

    def build_arch(self, arch):
        # Call super() late
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            shprint(sh.mkdir, '-p', 'build/lib.' + 'linux-x86_64' + '-2.7/M2Crypto')
            #shprint(sh.sed, '-i', '89,89d', 'setup.py')
            #shprint(sh.sed, '-i', '90i\ \ \ \ \ \ \ \ self.swig_opts.append("-D__armeabi__")', 'setup.py')
            #shprint(sh.sed, '-i', '92i\ \ \ \ \ \ \ \ self.swig_opts.append("-v")', 'setup.py')
            hostpython = sh.Command(self.hostpython_location)
            # Build M2Crypto
            env['LDSHARED'] = '/home/paul/.local/lib/python2.7/site-packages/pythonforandroid/tools/liblink'
            shprint(hostpython,
                    'setup.py',
                    'build_ext',
                    '-v',
                    '-f',
                    #'-p' + arch.arch,
                    #'-c' + 'unix',
                    '-o' + env['OPENSSL_BUILD_PATH'],
                    '-L' + env['OPENSSL_BUILD_PATH']
            , _env=env)
            del env['LDSHARED']
        super(M2CryptoRecipe, self).build_arch(arch)

    def get_recipe_env(self, arch):
        env = super(M2CryptoRecipe, self).get_recipe_env(arch)
        env['OPENSSL_BUILD_PATH'] = self.get_recipe('openssl', self.ctx).get_build_dir(arch.arch)
        env['CFLAGS'] += ' -I' + join(self.ctx.get_python_install_dir(), 'include/python2.7')
        #env['MULTIARCH'] = arch.arch
        print env
        return env

recipe = M2CryptoRecipe()
