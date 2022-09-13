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

    qu = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for state in qu.all():
        print("{}: {}".format(state.id, state.name))
    session.close()
