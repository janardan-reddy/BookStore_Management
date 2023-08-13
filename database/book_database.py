from fastapi import HTTPException,status
from database.models import DBBook
from sqlalchemy.orm import Session

def getAllBooks(db):
    result= db.query(DBBook).all()
    return result

def getBookById(isbn: str, db:Session):
    result= db.query(DBBook).filter(DBBook.isbn == isbn).first()
    if result != None:
        return result
    else:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"Requested book does not found"
            )

def addBook(request:DBBook, db:Session):
    db.add(request)
    db.commit()
    db.refresh(request)
    return request

def updateBook(isbn: str, request: DBBook, db:Session):
    result= db.query(DBBook).filter(DBBook.isbn == isbn).first()
    if result != None:
        result.update(**request)
    else:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"Requested book does not found"
            )    

def deleteBook(isbn: str, db:Session):
    result= db.query(DBBook).filter(DBBook.isbn == isbn).first()
    if result != None:
        result.delete()
        db.commit()
    else:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"Requested book does not found"
            )
