import math
import random
from application.schemas.requests.book_request import BookRequest
from sqlalchemy.orm import Session
from database import book_database
from database.models import DBBook
from utils import common_utils

def getAllBooks(db:Session):
   result = book_database.getAllBooks(db)
   return result

def getBookById(id: str, db: Session):
   result = book_database.getBookById(id, db)
   return result

def addBook(request: BookRequest, db: Session):
   new_book = DBBook(
      isbn = generateRandomIsbnNumber(),
      author = request.author,
      title= request.title,
      price= request.price
      )     
   result = book_database.addBook(new_book,db)
   return result

def updateBook(isbn:str, request: BookRequest, db:Session):
   result= book_database.updateBook(isbn, request, db)
   return result

def deleteBook(isbn: str, db:Session):
   result= book_database.deleteBook(isbn, db)
   return result

def generateRandomIsbnNumber():
   return 'ISBN'+ common_utils.generateRandomNumber()