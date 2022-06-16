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

def query2():
    query='''
    MATCH (r:Recipient)<-[rel:HAS_RECEIVED]-(t:Transaction)
    WHERE t.time >= "2021-04-10 00:01:52" AND t.time <= "2021-04-10 00:01:53"
    RETURN r.recipient_id, rel.value, rel.value_usd
    '''

def query3(): 
    query=
    '''
    MATCH (t:Transaction)-[:BELONGS_TO]->(:Block {blockId: "678534"})
    RETURN count(t), sum(t.input_total), sum(t.output_total), sum(t.fee)
    '''

def query4(): 
    query=
    '''
    MATCH (r:Recipient)<-[:HAS_RECEIVED]-(t:Transaction)
    WHERE t.time ="2021-04-10 00:01:52"
    WITH t, count(t) AS numTransactions, r.recipient_id as recipient, collect(t.hash) as transactions
    WHERE  numTransactions = 3
    RETURN recipient, numTransactions, transactions
    '''

def query5(): 
    query=
    '''
    MATCH (r:Recipient)-[rel:HAS_GIVEN]->(:Transaction)
    WHERE r.recipient_id ="134RBvQhLnwzfGdUAzKkSy257e6kuokSe9" and rel.time = "2021-04-16 23:43:32"
    WITH rel, sum(rel.value_usd) AS totalValueUSD
    RETURN totalValueUSD
    '''

def query6(): 
    query=
    '''
    MATCH (in_r:Recipient)-[:HAS_GIVEN]->(t:Transaction)-[out_rel:HAS_RECEIVED]->(out_r:Recipient)
    WHERE t.time >= "2021-04-10 00:01:52" AND t.time <= "2021-04-10 00:03:53"
    WITH in_r.recipient_id as input_recipient, t.time as day, collect(out_r.recipient_id) as out_recipients, count(out_r.recipient_id) as out_count
    RETURN input_recipient, day, out_count, out_recipients
    ORDER BY out_count DESC LIMIT 5
    '''

def query7(): 
    query=
    '''
    MATCH (in_r:Recipient)-[in_rel:HAS_GIVEN*]->(t:Transaction)-[out_rel:HAS_RECEIVED*]->(out_r:Recipient)
    WHERE t.time >= "2021-04-10 00:01:52" AND t.time <= "2021-04-10 00:03:53"
    WITH in_r.recipient_id as input_recipient, out_r.recipient_id as output_recipient, SUM(out_rel.value_usd) as out_value, SUM(in_rel.value_usd) as in_value
    RETURN input_recipient, out_value + in_value AS total_value, output_recipient
    ORDER BY total_value DESC LIMIT 5
    '''

def query8(): 
    query=
    '''
    MATCH (r:Recipient)-[g:HAS_GIVEN]->(t:Transaction)-[:BELONGS_TO]->(b:Block)
    WHERE b.blockId = "679043" 
    WITH r.recipient_id as input_recipient, SUM(g.value_usd) as value_usd_agg, SUM(g.value) as value_agg
    RETURN input_recipient, MAX(value_usd_agg/value_agg) AS total_count, value_usd_agg, value_agg
    '''

def query9(): 
    query=
    '''
    '''

def query10(): 
    query=
    '''
    '''

def query11(): 
    query=
    '''
    '''

def query12(): 
    query=
    '''
    MATCH (g:Guessed_miner)<-[rel:REWARDED]-(b:Block)
    WHERE b.time >= "2021-04-10 00:01:52" AND b.time <= "2021-04-14 00:03:53"
    WITH collect(g.guessed_miner_id) as miner, rel
    RETURN miner, sum (rel.reward) as totalReward, count(rel) as numBlocks
    ORDER BY totalReward DESC LIMIT 5
    '''