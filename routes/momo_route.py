from flask import Blueprint,request
from . import make_response
from models.profile import ProfileModel
from configs.response_message import messages

momo_api = Blueprint("momo_route",__name__,url_prefix="/momo")


@momo_api.route('/mtn/callback',methods=["POST"])
def mtncallback():
    if not request.is_json:
        return make_response('0401','Error: json header',status=401)
    request_response = request.get_json()
    
    print(request_response)
    return make_response("200","mtn demo")