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

@varun.post()
def updateBook():
    pass

@varun.del()
def deleteBook():
    pass