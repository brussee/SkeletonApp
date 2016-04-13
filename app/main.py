
print sys.modules

import imp

try:
    print imp.find_module("_ssl")
    import _ssl
except ImportError:
    print("no _ssl")

print sys.modules

try:
    print imp.find_module("_sqlite3")
    import _sqlite3
except ImportError:
    print("no _sqlite3")

try:
    print imp.find_module("sqlite3")
    import sqlite3
except ImportError:
    print("no sqlite3")
