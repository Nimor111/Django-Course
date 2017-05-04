from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String, Integer

from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///pdfs.db')

Base = declarative_base()


class PDF(Base):
    __tablename__ = 'pdf'
    id = Column(Integer, primary_key=True)
    uuid = Column(String)
    path = Column(String)
    url = Column(String)


session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
