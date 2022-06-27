from flask import Flask, jsonify, request
import queries 

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error=None):
    resp = jsonify("Not Found " + request.url)
    resp.status_code = 404
    return resp

@app.route('/query1', methods = ['GET'])
def _query1():
    args = request.args
    _hash_ = args.get("hash", type=str)
    
    if _hash_ and request.method == 'GET':
        res = queries.query1(_hash_)
        return res
    else:
        return not_found()

@app.route('/query2', methods = ['GET'])
def _query2():
    args = request.args
    _datefrom_ = args.get("datefrom", type=str)
    _dateto_ = args.get("dateto", type=str)

    if _datefrom_ and _dateto_ and request.method == 'GET':
        res = queries.query2(_datefrom_, _dateto_)
        return res
    else:
        return not_found()

@app.route('/query3', methods = ['GET'])
def _query3():
    args = request.args
    _blockId_ = args.get("blockId", type=str)
    
    if _blockId_ and request.method == 'GET':
        res = queries.query3(_blockId_)
        return res
    else:
        return not_found()

@app.route('/query4', methods = ['GET'])
def _query4():
    args = request.args
    _day_ = args.get("day", type=str)
    _numTransactions_ = args.get("numTransactions", type=int)

    if _day_ and _numTransactions_ and request.method == 'GET':
        res = queries.query4(_day_, _numTransactions_)
        return res
    else:
        return not_found()

@app.route('/query5', methods = ['GET'])
def _query5():
    args = request.args
    _day_ = args.get("day", type=str)
    _input_recipient_ = args.get("input_recipient", type=str)

    if _day_ and _input_recipient_ and request.method == 'GET':
        res = queries.query5(_day_, _input_recipient_)
        return res
    else:
        return not_found()

@app.route('/query6', methods = ['GET'])
def _query6():
    args = request.args
    _datefrom_ = args.get("datefrom", type=str)
    _dateto_ = args.get("dateto", type=str)
    _topk_ = args.get("topk", type=int)

    if _datefrom_ and _dateto_ and _topk_ and request.method == 'GET':
        res = queries.query6(_datefrom_, _dateto_, _topk_)
        return res
    else:
        return not_found()

@app.route('/query7', methods = ['GET'])
def _query7():
    args = request.args
    _datefrom_ = args.get("datefrom", type=str)
    _dateto_ = args.get("dateto", type=str)
    _topk_ = args.get("topk", type=int)

    if _datefrom_ and _dateto_ and _topk_ and request.method == 'GET':
        res = queries.query7(_datefrom_, _dateto_, _topk_)
        return res
    else:
        return not_found()

@app.route('/query8', methods = ['GET'])
def _query8():
    args = request.args
    _block_ = args.get("block", type=str)

    if _block_ and request.method == 'GET':
        res = queries.query8(_block_)
        return res
    else:
        return not_found()

@app.route('/query10', methods = ['GET'])
def _query10():
    args = request.args
    _dayfrom_ = args.get("dayfrom", type=str)
    _dayto_ = args.get("dayto", type=str)
    _topk_ = args.get("topk", type=int)

    if _dayfrom_ and _dayto_ and _topk_ and request.method == 'GET':
        res = queries.query10(_dayfrom_, _dayto_, _topk_)
        return res
    else:
        return not_found()

@app.route('/query11', methods = ['GET'])
def _query11():
    args = request.args
    _datefrom_ = args.get("datefrom", type=str)
    _dateto_ = args.get("dateto", type=str)

    if _datefrom_ and _dateto_ and request.method == 'GET':
        res = queries.query11(_datefrom_, _dateto_)
        return res
    else:
        return not_found()

@app.route('/query12', methods = ['GET'])
def _query12():
    args = request.args
    _datefrom_ = args.get("datefrom", type=str)
    _dateto_ = args.get("dateto", type=str)
    _topk_ = args.get("topk", type=int)

    if _datefrom_ and _dateto_ and _topk_ and request.method == 'GET':
        res = queries.query12(_datefrom_, _dateto_, _topk_)
        return res
    else:
        return not_found()

if __name__ == '__main__':
    app.run()