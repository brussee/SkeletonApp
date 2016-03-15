from pythonforandroid.toolchain import PythonRecipe, shprint, shutil, current_directory
from os.path import join, exists
import sh

class LibTriblerRecipe(PythonRecipe):
    version = '6.5.0'
    url = 'https://github.com/Tribler/tribler/releases/download/v{version}/Tribler-v{version}.tar.xz'
    depends = ['apsw', 'libsodium', 'libtorrent', 'm2crypto', 'netifaces',
               'openssl', 'pyasn1', 'pil', 'pyleveldb', 'python2', 'twisted']
    opt_depends = ['vlc']

recipe = LibTriblerRecipe()