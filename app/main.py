from time import sleep

print sys.modules

import imp

try:
    print imp.find_module("_ssl")
    import _ssl
except ImportError:
    print("no _ssl")

print sys.modules

try:
    print imp.find_module("_sqlite", "/data/user/0/org.tribler.android/files/")
    import _sqlite
except ImportError:
    print("no _sqlite")

try:
    print imp.find_module("sqlite", "/data/user/0/org.tribler.android/files/")
    import sqlite
except ImportError:
    print("no sqlite")

try:
    print imp.find_module("_sqlite3", "/data/user/0/org.tribler.android/files/")
    import _sqlite3
except ImportError:
    print("no _sqlite3")

try:
    print imp.find_module("sqlite3", "/data/user/0/org.tribler.android/files/")
    import sqlite3
except ImportError:
    print("no sqlite3")

sleep(1000000)