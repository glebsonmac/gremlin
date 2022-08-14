# from tkinter import E
from http.client import responses
import asyncio
from func import db_connection
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
# id = T.id
app = FastAPI()
# # g = db_connection()
# # @app.get("/" ,tags=["root"])
# async def root():
#     return {"message": "API ALIVE"}

@app.get("/get_authors_names", tags=["Author"])
async def get_names():
    try:
        response = await db_connection()
        print(response)
        return  response 
    except Exception as e:
        print(e)
        return {"message": "API ERROR", "message": e}

# asyncio.run(get_names())
