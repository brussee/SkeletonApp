try:
    import sqlite3
except ImportError:
    print("no sqlite3")
try:
    import _sqlite3
except ImportError:
    print("no _sqlite3")