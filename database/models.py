from database.database import Base
from sqlalchemy import Column,Integer,String, Float

class DBBook(Base):
    __tablename__ = 'book'
    id= Column(String, primary_key=True, index=True)
    isbn = Column(String)
    title= Column(String)
    price= Column(Float)
    author= Column(String)

class DBAuthor(Base):
    __tablename__= 'author'
    fullname= Column(String)
    id= Column(Integer, primary_key= True, index= True)
    zonal= Column(String)