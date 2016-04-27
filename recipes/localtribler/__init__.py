from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists, islink
from sh import mkdir, cp


class LocalTriblerRecipe(PythonRecipe):

    version = 'local'
    depends = ['android', 'apsw', 'cherrypy', 'cryptography', 'decorator',
               'feedparser', 'ffmpeg', 'libnacl', 'libsodium', 'libtorrent',
               'm2crypto', 'netifaces', 'openssl', 'pyasn1', 'pil', 'pyleveldb',
               'python2', 'requests', 'twisted']


    def should_build(self, arch):
        # Overwrite old build
        return True


    def prebuild_arch(self, arch):
        # Remove from site-packages
        PythonRecipe.clean_build(self, arch.arch)

        # Create empty build dir
        container_dir = self.get_build_container_dir(arch.arch)
        mkdir('-p', container_dir)

        with current_directory(container_dir):
            # Copy source from working copy
            cp('-rf', '/home/paul/repos/tribler', self.name)

        PythonRecipe.prebuild_arch(self, arch)


    def build_arch(self, arch):
        super(LibTriblerRecipe, self).build_arch(arch)
        # Install ffmpeg binary
        shutil.copyfile(self.get_recipe('ffmpeg', self.ctx).get_build_bin(arch),
                        join(self.ctx.dist_dir, 'ffmpeg'))


recipe = LocalTriblerRecipe()