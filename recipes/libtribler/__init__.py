from pythonforandroid.toolchain import Recipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

"""
Privacy with BitTorrent and resilient to shut down http://www.tribler.org
"""
class LibTriblerRecipe(PythonRecipe):

    version = 'devel'

    url = 'git+https://github.com/Tribler/tribler.git'

    depends = ['android', 'apsw', 'cherrypy', 'cryptography', 'decorator',
               'feedparser', 'ffmpeg', 'libnacl', 'libsodium', 'libtorrent',
               'm2crypto', 'netifaces', 'openssl', 'pyasn1', 'pil', 'pyleveldb',
               'python2', 'requests', 'twisted']

    site_packages_name = 'Tribler'

    def build_arch(self, arch):
        super(LibTriblerRecipe, self).build_arch(arch)
        # Install ffmpeg binary
        shutil.copyfile(self.get_recipe('ffmpeg', self.ctx).get_build_bin(arch),
                        join(self.ctx.dist_dir, 'ffmpeg'))


recipe = LibTriblerRecipe()