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

# print(asyncio.run(db_connection()))