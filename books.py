from fastapi import FastAPI, HTTPException
from pydantic import basemodel, Field

varun = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length = 1)
    author: str = Field(min_length = 1, max_length = 100)
    description: str = Field(min_length = 1, max_length = 100)
    rating: int = Field(gt=-1, lt=101)

books = []

@varun.get("/")
def read_api():
    return {'Welcome': 'Varun'}

@varun.put("/")
def createBook():
    pass

@varun.post("")
def updateBook(book_id: UUID, book: BOOK):
    counter = 0
    for x in books:
        if x.id == book_id:
            books[counter - 1] = book
            return books[counter - 1]
    raise htt

@varun.del()
def deleteBook():
    pass