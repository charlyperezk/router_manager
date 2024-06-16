from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine


Base = declarative_base()
engine = create_engine("sqlite:///./test.db")

def create_db():
    Base.metadata.create_all(engine, checkfirst=True)

def get_session():
    session = Session(bind=engine)
    return session
    # try:
    #     yield session
    # finally:
    #     session.close()
