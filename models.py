from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker


from sqlalchemy.orm import declarative_base
Base = declarative_base()
  
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
  
  
class Hero(Base):
    __tablename__ = 'heroes'
    id = Column(Integer, primary_key=True)
    name = Column(String)

