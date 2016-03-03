#!/usr/bin/env python

import apsw
import sys

write=sys.stdout.write

write("                Python "+sys.executable+" "+str(sys.version_info)+"\n")
write("Testing with APSW file "+apsw.__file__+"\n")
write("          APSW version "+apsw.apswversion()+"\n")
write("    SQLite lib version "+apsw.sqlitelibversion()+"\n")
write("SQLite headers version "+str(apsw.SQLITE_VERSION_NUMBER)+"\n")
write("    Using amalgamation "+str(apsw.using_amalgamation)+"\n")

if [int(x) for x in apsw.sqlitelibversion().split(".")]<[3,7,8]:
    write("You are using an earlier version of SQLite than recommended\n")

sys.stdout.flush()
