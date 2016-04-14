from imp import find_module

print sys.builtin_module_names

try:
    import _ssl
except ImportError:
    print("no _ssl")
print find_module("_ssl")

print sys.modules

try:
    import _sqlite
except ImportError:
    print("no _sqlite")
print find_module("_sqlite", "/data/user/0/org.tribler.android/files/")

try:
    import sqlite
except ImportError:
    print("no sqlite")
print find_module("sqlite", "/data/user/0/org.tribler.android/files/")

try:
    import _sqlite3
except ImportError:
    print("no _sqlite3")
print find_module("_sqlite3", "/data/user/0/org.tribler.android/files/")

try:
    import sqlite3
except ImportError:
    print("no sqlite3")
print find_module("sqlite3", "/data/user/0/org.tribler.android/files/")

from time import sleep
sleep(1000000)