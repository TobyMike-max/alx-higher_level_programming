#!/usr/bin/python3
""" Lists all cities of a state from the database hbtn_0e_4_usa.
        Usage: ./5-filter_cities.py <mysql username> \
                                        <mysql password> \
                                        <database name>  \
                                        <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states
                ON cities.state_id=states.id
                WHERE states.name LIKE %s
                ORDER BY cities.id", (arg[4],))
    for city in cur.fetchall():
        print(", ".join(city[0]))
    cur.close()
    db.close()
