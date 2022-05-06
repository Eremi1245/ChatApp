from select import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session

from utility.const import CONNECT_TO_DB


def get_session() -> Session:
    engine = create_engine(CONNECT_TO_DB)
    Session = sessionmaker()
    Session.configure(bind=engine,autoflush=True)

    sess = Session()
    # engine = create_engine('mysql+pymysql://root:1234@localhost/python_chat')
    return sess
