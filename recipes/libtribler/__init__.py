from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class LibTriblerRecipe(PythonRecipe):
    version = '6.5.0'
    url = 'https://github.com/Tribler/tribler/archive/v{version}.tar.gz'
    depends = ['apsw', 'cherrypy', 'libnacl', 'libsodium', 'libtorrent', 'm2crypto', 'netifaces',
               'openssl', 'pyasn1', 'pil', 'pyleveldb', 'python2', 'requests', 'twisted']
    opt_depends = ['vlc']

recipe = LibTriblerRecipe()
