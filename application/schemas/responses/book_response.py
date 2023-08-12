from pydantic import BaseModel

class BookResponse(BaseModel):
    class config():
        orm_mode= True
    
    title: str
    isbn: str
    price: float
    author: str