#!/usr/bin/python3
"""Script that lists all State objects from
 the database htbn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    usr = session.query(State).filter(User.name == sys.argv[4]).first()
    if usr:
        print('{}'.format(usr.id))
    print('Not found')
    session.close()
