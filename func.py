from gremlin_python.process.anonymous_traversal import traversal
# from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from goblin import DriverRemoteConnection
from goblin import Graph
import asyncio

async def db_connection():
    remote_connection = await DriverRemoteConnection.open('ws://172.17.0.2:8182/gremlin', 'g')
    g = Graph().traversal().withRemote(remote_connection)
    print('connection established')
    vertices = await g.V().hasLabel('Author').properties('name').toList()
    await remote_connection.close()
    return vertices

async def add_author(name,id):
    remote_connection = await DriverRemoteConnection.open('ws://172.17.0.2:8182/gremlin', 'g')
    g = Graph().traversal().withRemote(remote_connection)
    print('connection established')
    vertices = await g.addV('Author').property('id', id).property('name', name).next()
    await remote_connection.close()
    return vertices

async def remove_author(id):
    remote_connection = await DriverRemoteConnection.open('ws://172.17.0.2:8182/gremlin', 'g')
    g = Graph().traversal().withRemote(remote_connection)
    print('connection established')
    vertices = await g.V(id).drop().next()
    await remote_connection.close()
    return vertices


async def add_book( id, name, isbn ,quantity):
    remote_connection = await DriverRemoteConnection.open('ws://172.17.0.2:8182/gremlin', 'g')
    g = Graph().traversal().withRemote(remote_connection)
    print('connection established') 
    vertices = await g.addV('book').property('id', id).property('name', name).property('isbn', isbn).property('quantity', quantity).next()
    await remote_connection.close()
    return vertices