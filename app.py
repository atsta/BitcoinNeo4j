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
    _hash_ = args.get("hash", type=str)
    
    if _hash_ and request.method == 'GET':
        res = queries.query1(_hash_)
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

if __name__ == '__main__':
    app.run()