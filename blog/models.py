from database import Base
from sqlalchemy import Column, Integer, String

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key = True, index=True)
    title = Column(String(30))
    desc = Column(String(30))


class Blog1(Base):
    __tablename__ = 'blogs1'
    id = Column(Integer, primary_key = True, index=True)
    title = Column(String(30))
    desc = Column(String(30))


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True, index=True)
    name =  Column(String(30))
    email = Column(String(30))
    password = Column(String(30))    


class UserData(Base):
    __tablename__ = "UsersData"
    id = Column(Integer, primary_key = True, index=True)
    name =  Column(String(30))
    email = Column(String(30))
    password = Column(String(300))     