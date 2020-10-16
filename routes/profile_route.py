from flask import Blueprint,request
from . import make_response
from models.profile import ProfileModel
from configs.response_message import messages

profile_api = Blueprint("profile_route",__name__,url_prefix="/profile")


@profile_api.route('/add',methods=["POST"])
def add():
    if not request.is_json:
        return make_response('0401','Error: json header',status=401)
    request_response = request.get_json()
    required_fields = ['username','email','password']
    for field in required_fields:
        if field not in request_response.keys():
            return make_response(messages.get('00300'),messages.get('00300').get('en'),status=401)
    added = ProfileModel.add(request_response.get('username'),request_response.get('email'),request_response.get('password'))
    if added:
        return  make_response(messages.get('00200'),messages.get('00200').get('en'),status=200)
    return make_response(messages.get('00300'),messages.get('00300').get('en'),status=200)
    
@profile_api.route('/login',methods= ['POST'])
def login():
    if not request.is_json:
        return  make_response(messages.get('00401'),messages.get('00401').get('en'),status=401)
    request_response = request.get_json()
    required_fields = ['email','password']
    for field in required_fields:
        if field not in request_response.keys():
            return make_response(messages.get('00300'),messages.get('00300').get('en'),status=401)
        
    logined = ProfileModel.login(request_response.get('email'),request_response.get('password'))
    if logined:
        return make_response(messages.get('01200'),messages.get('01200').get('en'),status=200)
    return make_response(messages.get('01300'),messages.get('01300').get('en'),status=401)