from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists, islink
from sh import rm, cp

class LibTriblerRecipe(PythonRecipe):
    version = 'working-copy'
    depends = ['android', 'apsw', 'cherrypy', 'cryptography', 'decorator',
               'feedparser', 'libnacl', 'libsodium', 'libtorrent', 'm2crypto',
               'netifaces', 'openssl', 'pyasn1', 'pil', 'pyleveldb', 'python2',
               'requests', 'twisted']
    opt_depends = ['vlc', ('ffmpeg', 'libav-tools')]

    def should_build(self, arch):
        # Overwrite old build
        return True

    def prebuild_arch(self, arch):
        # Remove from site-packages
        PythonRecipe.clean_build(self, arch.arch)

        with current_directory(self.get_build_container_dir(arch.arch)):
            rm('-rf', self.name)
            # Copy source from working copy
            cp('-rf', '/home/paul/repos/tribler', self.name)

        PythonRecipe.prebuild_arch(self, arch)

recipe = LibTriblerRecipe()
