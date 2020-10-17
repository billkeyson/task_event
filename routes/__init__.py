import json
from bson import json_util
from flask import Response,Flask
from flask_cors import CORS
from flask_socketio import SocketIO




def make_response(code,message,results={},status=200):
    if code == '1':
        status = 200
    elif code == '0':
        status = 401
    return Response(response=json.dumps({ 'message': {'code':code,'message':message}, 'results': results},
        default=json_util.default),
        status=status,
        mimetype="application/json")
    

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app,cors_allowed_origins="*")
    

