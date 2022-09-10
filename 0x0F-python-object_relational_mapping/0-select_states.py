#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
