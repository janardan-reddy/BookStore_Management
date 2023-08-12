from fastapi import FastAPI
from application.routers import book_router,author_router
from database.models import Base
from database import models
from database.database import engine

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(book_router.router)
app.include_router(author_router.router)

@app.get('/')
def index():
    return {
        'status': 'success',
        'message': 'server is up and running'
    }