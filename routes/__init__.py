import json
from bson import json_util
from flask import Response





def make_response(code,message,results={},status=200):
    if code == '1':
        status = 200
    elif code == '0':
        status = 401
    return Response(response=json.dumps({ 'message': {'code':code,'message':message}, 'results': results},
        default=json_util.default),
        status=status,
        mimetype="application/json")