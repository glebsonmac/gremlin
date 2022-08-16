# from tkinter import E
from http.client import responses
import asyncio
import json
from schemas import Author, Book, removeAuthor, AuthorName
from func import get_authors, add_author, delete_author, add_books, get_books, get_author_by_name, update_author, update_books, delete_books, verifyName
from fastapi import Body, FastAPI, HTTPException, Depends , Query, Request
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from gremlin_python import statics
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
# from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import T
# from gremlin_python.process.traversal import Order
# from gremlin_python.process.traversal import Cardinality
# from gremlin_python.process.traversal import Column
from gremlin_python.process.traversal import Direction
# from gremlin_python.process.traversal import Operator
# from gremlin_python.process.traversal import P
# from gremlin_python.process.traversal import TextP
# from gremlin_python.process.traversal import Pop
# from gremlin_python.process.traversal import Scope
# from gremlin_python.process.traversal import Barrier
# from gremlin_python.process.traversal import Bindings
# from gremlin_python.process.traversal import WithOptions


# from_ = Direction.OUT
# to = Direction.IN
id = T.id
app = FastAPI()
# # g = get_authors()
# # @app.get("/" ,tags=["root"])
# async def root():
#     return {"message": "API ALIVE"}

@app.get("/get_all_authors", tags=["Author"])
async def get_all_authors():
    try:
        response = await get_authors()
        print(response)
        return  response
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}


@app.post("/get_authors_by_name", tags=["Author"])
async def get_authors_by_name(author:AuthorName):
    try:
        if verifyName(author.name):
            response = await get_author_by_name(author.name)
            print(response)
            return  response
        else:
            raise HTTPException(status_code=404, detail='please put the author name with the correct format')
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}

@app.post("/add_authors", tags=["Author"])
async def create_author(author:Author):
    try:
        author.id = id
        response = await add_author(author.name, author.id)
        print(response)
        return  True
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}

@app.post("/update_authors", tags=["Author"])
async def update_authors(author:Author):
    try:
        author.id = id
        response = await update_author(author.name, author.id)
        print(response)
        return  True
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}

@app.delete("/remove_authors", tags=["Author"])
async def remove_author(author:removeAuthor):
    try:
        response = await delete_author(author.id)
        print(response)
        return  True
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}


@app.post("/add_book", tags=["Book"])
async def add_book(book:Book):
    try:
        book.id = id
        response = await add_books(book.id, book.name, book.isbn,book.quantity)
        print(response)
        return  True
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}

@app.post("/update_book", tags=["Book"])
async def update_book(book:Book):
    try:
        book.id = id
        response = await update_books(book.id, book.name, book.isbn,book.quantity)
        print(response)
        return  True
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}

@app.delete("/remove_book", tags=["Book"])
async def remove_book(book:Book):
    try:
        book.id = id
        response = await delete_books(book.id, book.name, book.isbn,book.quantity)
        print(response)
        return  True
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}

@app.get("/get_book", tags=["Book"])
async def get_book():
    try:
        response = await get_books()
        print(response)
        return  response
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}