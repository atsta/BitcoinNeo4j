import os
import json
from py2neo import Graph

password = os.environ.get('GRAPH_PSW')
graph = Graph(password=password)

def query1():
    query = '''
    MATCH (n:Guessed_miner) RETURN n LIMIT 25
    '''
    res = graph.run(query)    
    return json.dumps(list(res))