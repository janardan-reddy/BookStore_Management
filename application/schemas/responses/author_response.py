from pydantic import BaseModel

class AuthorResponse(BaseModel):
    class config():
        orm_mode = True

    fullname: str
    zonal: str
    books_count: int