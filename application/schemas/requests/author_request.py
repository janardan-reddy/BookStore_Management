from pydantic import BaseModel
from typing import List,Optional
from application.schemas.requests.book_request import BookRequest

class Name(BaseModel):
    fName: str
    lName: str
    mName: str
class AuthorRequest(BaseModel):
    name: Name
    zonals: Optional[List[str]]
    books: Optional[List[BookRequest]]