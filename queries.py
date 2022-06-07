import os
import json
from py2neo import Graph

password = os.environ.get('GRAPH_PSW')
graph = Graph(password=password)

def query1(_hash_):
    query = '''
    MATCH (r:Recipient)-[rel:HAS_GIVEN]->(:Transaction {hash: $hash })
    RETURN r.recipient_id, rel.value, rel.value_usd
    '''
    res = graph.run(query, hash=_hash_)    
    return json.dumps(list(res))