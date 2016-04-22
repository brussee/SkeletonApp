from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists, dirname
import sh

class LibTriblerRecipe(PythonRecipe):
    version = 'working-copy'
    depends = ['apsw', 'cherrypy', 'cryptography', 'decorator', 'feedparser',
               'libnacl', 'libsodium', 'libtorrent', 'm2crypto', 'netifaces',
               'openssl', 'pyasn1', 'pil', 'pyleveldb', 'python2', 'requests',
               'twisted']
    opt_depends = ['vlc', ('ffmpeg', 'libav-tools')]

    def should_build(self, arch):
        # Overwrite old build
        return True

    def prebuild_arch(self, arch):
        # Remove empty build dir
        sh.rm('-rf', current_directory(self.get_build_dir(arch.arch)))
        with current_directory(self.get_build_container_dir(arch.arch)):
            # Use source from working copy
            sh.ln('-s', '/home/paul/repos/tribler', self.name)
        PythonRecipe.prebuild_arch(self, arch)

recipe = LibTriblerRecipe()
