from typing import List
from fastapi import APIRouter, Depends, status
from database.database import get_db
from application.schemas.responses.book_response import BookResponse
from application.schemas.requests.book_request import BookRequest
from sqlalchemy.orm import Session
from service import book_service

router = APIRouter(
    prefix= '/book',
    tags=['book']
)

@router.get('', status_code= status.HTTP_200_OK, response_model=List[BookResponse])
def getAllBooks(db:Session= Depends(get_db)):
    result = book_service.getAllBooks(db)
    return result

@router.get('/{isbn}', status_code=status.HTTP_200_OK, response_model=BookResponse)
def getBookById(isbn: str, db:Session= Depends(get_db)):
    result = book_service.getBookById(isbn, db)
    return result

@router.post('/add', status_code=status.HTTP_200_OK, response_model= BookResponse)
def addBook(request: BookRequest, db:Session = Depends(get_db)):
    result = book_service.addBook(request, db)    
    return result

@router.put('/update/{isbn}', status_code= status.HTTP_200_OK)
def updateBook(isbn: str, request: BookRequest, db:Session= Depends(get_db)):
    result= book_service.updateBook(isbn, BookRequest, db)
    return result

@router.delete('/delete/{isbn}', status_code= status.HTTP_204_NO_CONTENT)
def deleteBook(isbn: str, db:Session= Depends(get_db)):
    result= book_service.deleteBook(isbn, db)
    return result