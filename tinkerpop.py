from gremlin_python import statics
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
# from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import T
from gremlin_python.process.traversal import Order
from gremlin_python.process.traversal import Cardinality
from gremlin_python.process.traversal import Column
from gremlin_python.process.traversal import Direction
from gremlin_python.process.traversal import Operator
from gremlin_python.process.traversal import P
from gremlin_python.process.traversal import TextP
from gremlin_python.process.traversal import Pop
from gremlin_python.process.traversal import Scope
from gremlin_python.process.traversal import Barrier
from gremlin_python.process.traversal import Bindings
from gremlin_python.process.traversal import WithOptions
from goblin import DriverRemoteConnection
from goblin import Graph
import asyncio
import json
from_ = Direction.OUT
to = Direction.IN
# conn = DriverRemoteConnection('ws://172.17.0.2:8182/gremlin', 'g')
# g = traversal().withRemote(conn)
# def db_connection():
#     conn = DriverRemoteConnection('ws://172.17.0.2:8182/gremlin', 'g')
#     g = traversal().withRemote(conn)
#     print('connection established')
#     return g
id = T.id

async def db_connection():
    remote_connection = await DriverRemoteConnection.open('ws://172.17.0.2:8182/gremlin', 'g')
    g = Graph().traversal().withRemote(remote_connection)
    print('connection established')
    vertices = await g.V().hasLabel('Author').properties('name').toList()
    await remote_connection.close()
    return vertices

# person = g.addV('Author').property('id', '01').property('name', 'Ravi Raja').iterate();
# v1 = g.addV('Author').property('id', id).property('name', 'Ravi Raja').next()
# print(g.addV('Author').property('id', '01').property('name', 'Ravi Raja'))
# v2 = g.addV('Book').property('id', id).property('name', 'Ravi Raja').property('isbn','false').property('quantity',2).next()
# print(g.addV('Book').property('id', '01').property('name', 'Ravi Raja').property('isbn','false').property('quantity',2).next())
# g.addE("created").from_(v1).to(v2).property(id, 1)
# print(g.V('Author').values('name'))


print(json.dumps(asyncio.run(db_connection())))
# conn.close()
