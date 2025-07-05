from fastapi import FastAPI, HTTPException
from pydantic import basemodel, Field

varun = FastAPI()
books = []

@varun.get("/")
def read_api():
    return {'Welcome': 'Varun'}

@varun.put()
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