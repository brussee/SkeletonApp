from pythonforandroid.toolchain import PythonRecipe, shutil
from os.path import join
from sh import mkdir

"""
Privacy with BitTorrent and resilient to shut down

http://www.tribler.org
"""
class LibTriblerRecipe(PythonRecipe):

    version = 'devel'

    url = 'git+https://github.com/Tribler/tribler.git'

    depends = ['android', 'apsw', 'cherrypy', 'cryptography', 'decorator',
               'feedparser', 'ffmpeg', 'libnacl', 'libsodium', 'libtorrent',
               'm2crypto', 'netifaces', 'openssl', 'pyasn1', 'pil', 'pyleveldb',
               'python2', 'requests', 'twisted']

    site_packages_name = 'Tribler'

    def postbuild_arch(self, arch):
        super(LibTriblerRecipe, self).postbuild_arch(arch)
        # Install ffmpeg binary
        private_dir = join(self.ctx.dist_dir, 'TriblerApp', 'private')
        mkdir('-p', private_dir)
        shutil.copyfile(self.get_recipe('ffmpeg', self.ctx).get_build_bin(arch),
                        join(private_dir, 'ffmpeg'))


recipe = LibTriblerRecipe()