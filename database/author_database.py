from fastapi import HTTPException,status
from database.models import DBAuthor
from sqlalchemy.orm import Session

def getAllAuthors(db:Session):
    return db.query(DBAuthor).all()

def getAuthorById(id: str, db:Session):
    result = db.query(DBAuthor).filter(DBAuthor.id == id).first()
    if result != None:
        return result
    else:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"Requested Author does not found"
            )    

def addAuthor(request: DBAuthor, db:Session):
    db.add(request)
    db.commit()
    db.refresh(request)
    return request

def updateAuthor(id: str, request: DBAuthor, db:Session):
    result= db.query(DBAuthor.id == id).first()
    if result != None:
        result.update(**request)
        db.commit()
    else:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"Requested Author does not found"
            ) 
    
def deleteAuthor(id:str, db:Session):
    result= db.query(DBAuthor).filter(DBAuthor.id == id).first()
    if result != None:
        result.delete()
        db.commit()
    else:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"Requested Author does not found"
            ) 