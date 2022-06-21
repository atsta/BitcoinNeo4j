import os
import json
from py2neo import Graph

password = os.environ.get('GRAPH_PSW')
graph = Graph(password=password)

def query1(_hash_):
    query='''
    MATCH (r:Recipient)-[rel:HAS_GIVEN]->(:Transaction {hash: $hash })
    RETURN r.recipient_id, rel.value, rel.value_usd
    '''
    res = graph.run(query, hash=_hash_)    
    return json.dumps(list(res))

def query2(_datefrom_, _dateto_):
    query='''
    WITH apoc.date.convertFormat($datefrom, "yyyy-MM-dd'T'HH:mm:ss", 'yyyy-MM-dd HH:mm:ss') as datefrom, 
    apoc.date.convertFormat($dateto, "yyyy-MM-dd'T'HH:mm:ss", 'yyyy-MM-dd HH:mm:ss') as dateto
    MATCH (r:Recipient)<-[rel:HAS_RECEIVED]-(t:Transaction)
    WHERE t.time >= datefrom AND t.time <= dateto
    RETURN r.recipient_id, rel.value, rel.value_usd
    '''
    res = graph.run(query, datefrom=_datefrom_, dateto=_dateto_)    
    return json.dumps(list(res))

def query3(_blockId_): 
    query='''
    MATCH (t:Transaction)-[:BELONGS_TO]->(:Block {blockId: $blockId })
    RETURN COUNT(t), SUM(t.input_total), SUM(t.output_total), SUM(t.fee)
    '''
    return json.dumps(list(graph.run(query, blockId=_blockId_)))

def query4(_day_, _numTransactions_): 
    query='''
    WITH apoc.date.convertFormat($day, "yyyy-MM-dd", 'yyyy-MM-dd') as inputday
    MATCH (r:Recipient)<-[:HAS_RECEIVED]-(t:Transaction)
    WHERE t.time STARTS WITH inputday
    WITH t, count(t) AS numTransactions, r.recipient_id as recipient, collect(t.hash) as transactions
    WHERE  numTransactions=$num
    RETURN recipient,t.time, numTransactions, transactions
    '''
    res = graph.run(query, day=_day_, num=_numTransactions_)  
    return json.dumps(list(res))

def query5(_day_, _input_recipient_): 
    query='''
    WITH apoc.date.convertFormat($day, "yyyy-MM-dd", 'yyyy-MM-dd') as inputday
    MATCH (r:Recipient)-[rel:HAS_GIVEN]->(:Transaction)
    WHERE r.recipient_id=$input_recipient AND rel.time STARTS WITH inputday
    WITH SUM(rel.value_usd) AS totalValueUSD
    RETURN totalValueUSD
    '''
    return json.dumps(list(graph.run(query, day=_day_, input_recipient=_input_recipient_)))

def query6(_datefrom_, _dateto_, _topk_): 
    query='''
    WITH apoc.date.convertFormat($datefrom, "yyyy-MM-dd'T'HH:mm:ss", 'yyyy-MM-dd HH:mm:ss') as datefrom, 
    apoc.date.convertFormat($dateto, "yyyy-MM-dd'T'HH:mm:ss", 'yyyy-MM-dd HH:mm:ss') as dateto
    MATCH (in_r:Recipient)-[:HAS_GIVEN]->(t:Transaction)-[out_rel:HAS_RECEIVED]->(out_r:Recipient)
    WHERE t.time >= datefrom AND t.time <= dateto
    WITH in_r.recipient_id as input_recipient, t.time as day, collect(out_r.recipient_id) as out_recipients, count(out_r.recipient_id) as out_count
    RETURN input_recipient, day, out_count, out_recipients
    ORDER BY out_count DESC LIMIT $topK
    '''
    return json.dumps(list(graph.run(query, datefrom=_datefrom_, dateto=_dateto_, topK=_topk_)))

def query7(_datefrom_, _dateto_, _topk_): 
    query='''
    WITH apoc.date.convertFormat($datefrom, "yyyy-MM-dd'T'HH:mm:ss", 'yyyy-MM-dd HH:mm:ss') as datefrom, 
    apoc.date.convertFormat($dateto, "yyyy-MM-dd'T'HH:mm:ss", 'yyyy-MM-dd HH:mm:ss') as dateto
    MATCH (in_r:Recipient)-[in_rel:HAS_GIVEN*]->(t:Transaction)-[out_rel:HAS_RECEIVED*]->(out_r:Recipient)
    WHERE t.time >= datefrom AND t.time <= dateto
    WITH in_r.recipient_id as input_recipient, out_r.recipient_id as output_recipient, 
    reduce(out_total = 1, r IN out_rel | out_total + r.value_usd) AS out_total, 
    reduce(in_total = 1, r IN in_rel | in_total + r.value_usd) AS in_total
    RETURN input_recipient, out_total+in_total as total, output_recipient
    ORDER BY total DESC LIMIT $topK
    '''
    return json.dumps(list(graph.run(query, datefrom=_datefrom_, dateto=_dateto_, topK=_topk_)))

def query8(): 
    query='''
    MATCH (r:Recipient)-[g:HAS_GIVEN]->(t:Transaction)-[:BELONGS_TO]->(b:Block {blockId: "679043"})
    WITH r.recipient_id as input_recipient, SUM(g.value_usd) as value_usd_agg, SUM(g.value) as value_agg
    RETURN input_recipient, MAX(value_usd_agg/value_agg) AS total_count, value_usd_agg, value_agg
    '''

def query9(): 
    query='''
    '''

def query10(): 
    query='''
    '''

def query11(_datefrom_, _dateto_): 
    query='''
    WITH apoc.date.convertFormat($datefrom, "yyyy-MM-dd'T'HH:mm:ss", 'yyyy-MM-dd HH:mm:ss') as datefrom, 
    apoc.date.convertFormat($dateto, "yyyy-MM-dd'T'HH:mm:ss", 'yyyy-MM-dd HH:mm:ss') as dateto
    MATCH (in_r:Recipient)-[:HAS_GIVEN]->(t:Transaction)-[out_rel:HAS_RECEIVED]->(out_r:Recipient)
    WHERE t.time >= datefrom AND t.time <= dateto
    WITH t.hash as transaction, COUNT(in_r.recipient_id) as in_count, COUNT(out_r.recipient_id) as out_count, datefrom, dateto
    WITH MAX(in_count + out_count) AS max_count, datefrom, dateto
    MATCH (in_r:Recipient)-[:HAS_GIVEN]->(t:Transaction)-[out_rel:HAS_RECEIVED]->(out_r:Recipient)
    WHERE t.time >= datefrom AND t.time <= dateto
    WITH t as transaction, COUNT(in_r.recipient_id) as in_count, COUNT(out_r.recipient_id) as out_count, max_count
    WHERE out_count + in_count = max_count 
    RETURN transaction.hash as max_transaction_hash, max_count, transaction.input_total as input_total, 
    transaction.output_total as output_total, transaction.fee as fee, transaction.time as time
    '''

    res = graph.run(query, datefrom=_datefrom_, dateto=_dateto_)    
    return json.dumps(list(res))

def query12(_datefrom_, _dateto_, _topk_): 
    query='''
    WITH apoc.date.convertFormat($datefrom, "yyyy-MM-dd'T'HH:mm:ss", 'yyyy-MM-dd HH:mm:ss') as datefrom, 
    apoc.date.convertFormat($dateto, "yyyy-MM-dd'T'HH:mm:ss", 'yyyy-MM-dd HH:mm:ss') as dateto
    MATCH (g:Guessed_miner)<-[rel:REWARDED]-(b:Block)
    WHERE b.time >= datefrom AND b.time <= dateto
    WITH collect(g.guessed_miner_id) as miner, rel
    RETURN miner, sum (rel.reward) as totalReward, count(rel) as numBlocks
    ORDER BY totalReward DESC LIMIT 5
    '''
    res = graph.run(query, datefrom=_datefrom_, dateto=_dateto_, topK=_topk_)    
    return json.dumps(list(res))