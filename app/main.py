from imp import find_module

print sys.builtin_module_names

try:
    print find_module("ssl")
    import ssl
except ImportError:
    print("no ssl")

try:
    print find_module("_ssl")
    import _ssl
except ImportError:
    print("no _ssl")

try:
    print find_module("sqlite3")
    import sqlite3
except ImportError:
    print("no sqlite3")

try:
    print find_module("_sqlite3")
    import _sqlite3
except ImportError:
    print("no _sqlite3")

try:
    print find_module("sqlite")
    import sqlite
except ImportError:
    print("no sqlite")

try:
    print find_module("_sqlite")
    import _sqlite
except ImportError:
    print("no _sqlite")

print sys.modules

from time import sleep

sleep(1000000)