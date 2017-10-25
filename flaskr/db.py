from flask import Flask

from flask_sqlalchemy import SQLAlchemy
#from ..models import conn
conn = 'mssql+pymssql://sa:123456@172.18.16.187/ZOUHUI-Dev'
#print(conn)
# create our little application :)
app = Flask(__name__)

db = SQLAlchemy(app)

from sqlalchemy import create_engine as _create_engine
import pymssql as _pymssql
try:
    _engine = _create_engine(conn, echo=False, max_overflow=10, pool_size=5)
    print('Database engine created.')
except Exception as e:
    print(str(e))
    _sys.exit()


# initialize Base
from sqlalchemy.ext.declarative import declarative_base as _declarative_base
Base = _declarative_base()


# define session scope
from contextlib import contextmanager as _contextmanager
from sqlalchemy.orm import scoped_session as _scoped_session
from sqlalchemy.orm import sessionmaker as _sessionmaker
Session = _sessionmaker()
Session.configure(bind=_engine)

@_contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        print(str(e))
    finally:
        session.close()