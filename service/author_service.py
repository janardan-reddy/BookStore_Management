from application.schemas.requests.author_request import AuthorRequest
from database.models import DBAuthor
from sqlalchemy.orm import Session
from database import author_database
from utils import common_utils

def getAllAuthors(db:Session):
    result = author_database.getAllAuthors(db)
    return result

def getAuthorById(id: str, db:Session):
    result = author_database.getAuthorById(id, db)
    return result

def addAuthor(request: AuthorRequest, db:Session):
    new_author = DBAuthor(
        fullname = f"{request.name.fName} {request.name.mName} {request.name.lName}",
        zonal = ','.join(request.zonals),
        id= generateRandomAuthorNumber()
    )
    result = author_database.addAuthor(new_author,db)
    return result

def updateAuthor(id, request: AuthorRequest, db:Session):
    result= author_database.updateAuthor(id, request, db)
    return result

def deleteAuthor(id: str, db:Session):
    result= author_database.deleteAuthor(id, db)
    return result

def generateRandomAuthorNumber():
    return 'Auth'+ common_utils.generateRandomNumber()