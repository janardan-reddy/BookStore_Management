from fastapi import APIRouter,Depends,status
from application.schemas.responses.book_response import BookResponse
from sqlalchemy.orm import Session
from application.schemas.requests.author_request import AuthorRequest
from application.schemas.responses.author_response import AuthorResponse
from database.database import get_db
from service import author_service
from typing import List

router = APIRouter(
    prefix='/author',
    tags=['author']
)

@router.get('/', response_model=List[AuthorResponse])
def getAllAuthors(db:Session = Depends(get_db)):
    return author_service.getAllAuthors(db)

@router.get('/{id}', status_code= status.HTTP_200_OK, response_model=BookResponse)
def getAuthorById(id: str, db:Session= Depends(get_db)):
    result= author_service.getAuthorById(id, db)
    return result

@router.post('/add', status_code= status.HTTP_201_CREATED, response_model=AuthorResponse)
def addAuthor(request: AuthorRequest, db:Session = Depends(get_db)):
    result = author_service.addAuthor(request, db)
    return result

@router.put('/update/{id}', status_code= status.HTTP_200_OK)
def updateAuthor(id: str, request: AuthorRequest, db:Session= Depends(get_db)):
    result= author_service.updateAuthor(id, request, db)
    return result

@router.delete('/delete/{id}', status_code= status.HTTP_204_NO_CONTENT)
def deleteAuthor(id: str, db:Session= Depends(get_db)):
    result= author_service.deleteAuthor(id, db)
    return result