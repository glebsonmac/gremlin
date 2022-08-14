# from tkinter import E
from http.client import responses
import asyncio
import json
from schemas import Author, Book, removeAuthor
from func import db_connection, add_author, remove_author, add_book
from fastapi import Body, FastAPI, HTTPException, Depends , Query, Request
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
# # g = db_connection()
# # @app.get("/" ,tags=["root"])
# async def root():
#     return {"message": "API ALIVE"}

@app.get("/get_authors", tags=["Author"])
async def get_names():
    try:
        response = await db_connection()
        print(response)
        return  response
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

@app.delete("/remove_authors", tags=["Author"])
async def remove_author(author:removeAuthor):
    try:
        response = await remove_author(author.id)
        print(response)
        return  True
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}


@app.post("/add_book", tags=["Book"])
async def create_book(book:Book):
    try:
        book.id = id
        response = await add_book(book.id, book.name, book.isbn,book.quantity)
        print(response)
        return  True
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}