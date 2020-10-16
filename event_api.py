from flask import Flask,request
from flask_socketio import SocketIO
from flask_cors import CORS
import json 
from werkzeug.exceptions import HTTPException

from routes import (
    make_response,
    profile_route,
    customer_route,
    job_route
)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app)

# Route Blueprints
app.register_blueprint(profile_route.profile_api)
app.register_blueprint(customer_route.customer_api)
app.register_blueprint(job_route.job_api)

@app.route('/')
def test():
    return make_response('code','server working! 0.0.1')

@app.errorhandler(500)
@app.errorhandler(HTTPException)
def server_error(e):
    return make_response("code","error",results ={'error':'Internal Server Error! Contact Admin'},status=500)
    

@app.errorhandler(404)
def page_not_found(e):
    return make_response("code","page error",results ={"error": "Page Not Found"},status=404)

@app.errorhandler(400)
def json_format(e):
    return make_response("code","request body error",results ={"error": "Page Not Found"},status=400)

if __name__ == "__main__":
      socketio.run(app,'0.0.0.0',port=5002)
    