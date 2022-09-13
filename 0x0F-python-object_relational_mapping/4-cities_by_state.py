#!/usr/bin/python3
"""
Script that lists all cities from database hbtn_0e_4_usa.
Takes three arguments. Usage:
                                ./4-cities_by_states.py
                                <mysql username>
                                <mysql password>
                                <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
    cur = db.cursor()
<<<<<<< HEAD
    cur.execute("SELECT * FROM cities JOIN (SELECT name FROM states)")
=======
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` FROM `cities` as `c` \
                    INNER JOIN `states` as `s` \
                    ON `c`.`state_id` = `s`.`id` \
                    ORDER BY `c`.`id`")
>>>>>>> 3f395ba91ca635c12770fb1669cb4a1fdbd9494f
    for state in cur.fetchall():
        print(state)