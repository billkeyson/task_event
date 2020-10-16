from flask import Flask,request
from flask_socketio import SocketIO
from flask_cors import CORS
import json 
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

if __name__ == "__main__":
      socketio.run(app,'0.0.0.0',port=5002)
    