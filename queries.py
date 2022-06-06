from neo4j import GraphDatabase
import os
import json

uri = "neo4j://localhost:7687"
user = os.environ.get('GRAPH_USR')
password = os.environ.get('GRAPH_PSW')
driver = GraphDatabase.driver(uri, auth=(user, password))
session = driver.session()

def query1(start_date, end_date):
    query = '''
    MATCH 
    '''
    res = session.run(query)
    return json.dumps(list(res))