from imp import find_module

print sys.builtin_module_names

try:
    import ssl
except ImportError:
    print("no ssl")

try:
    import _ssl
except ImportError:
    print("no _ssl")

try:
    import sqlite3
except ImportError:
    print("no sqlite3")

try:
    import _sqlite3
except ImportError:
    print("no _sqlite3")

try:
    import sqlite
except ImportError:
    print("no sqlite")

try:
    import _sqlite
except ImportError:
    print("no _sqlite")

print sys.modules

from time import sleep

sleep(1000000)