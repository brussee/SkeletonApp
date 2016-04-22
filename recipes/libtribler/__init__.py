from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists, islink
from sh import rm, ln

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
        build_dir = self.get_build_dir(arch.arch)

        if not islink(build_dir):
            # Remove empty build dir
            rm('-rf', build_dir)

            with current_directory(self.get_build_container_dir(arch.arch)):
                # Use source from working copy
                ln('-s', '/home/paul/repos/tribler', self.name)

        PythonRecipe.prebuild_arch(self, arch)

recipe = LibTriblerRecipe()
