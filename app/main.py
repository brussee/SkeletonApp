try:
    import _ssl
except ImportError:
    print("no _ssl")

try:
    import _sqlite3
except ImportError:
    print("no _sqlite3")

try:
    import sqlite3
except ImportError:
    print("no sqlite3")
