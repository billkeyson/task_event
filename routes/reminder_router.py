from flask import Blueprint,request
from . import make_response
from configs.response_message import messages
from models.reminder import ReminderModel
from flask_socketio import send, emit
import json
from . import socketio,make_response
reminder_api = Blueprint('reminder_api',__name__,url_prefix="/reminder")
@socketio.on('my event')
@reminder_api.route('/add',methods=['POST'])
def add():
    # start_date,end_date,service_type,interval
    if not request.is_json:
        return make_response('00414',messages.get('00414').get('en'),status=401)
    request_response = request.get_json()
    required_fields = ['service_type','job_id','start_date','interval','end_date']
    for field in required_fields:
        if field not in request_response.keys():
            return make_response('00400',messages.get('00400').get('en'),status=401)
    reminder = ReminderModel.add(request_response.get('start_date'),\
        request_response.get("end_date"),request_response.get("service_type"),request_response.get("interval"),request_response.get("job_id"))
    
    if reminder:
        socketio.emit("reminder_notification",reminder,namespace='/',include_self=True)
        return make_response('00200',messages.get('00200').get('en'),results={"uid":reminder},status=200)
    return make_response('00422',messages.get('00422').get('en'),results={},status=401)


@reminder_api.route('/')
def find_all():
    all_customer = ReminderModel.find()
    return make_response('00204',messages.get('00204').get('en'),results=all_customer)


@reminder_api.route('/<reminder_id>')
def find_a_job(reminder_id):
    a_job = ReminderModel.find_one(reminder_id)
    return make_response('00204',messages.get('00204').get('en'),results=a_job)



@reminder_api.route('/<reminder_id>',methods = ['DELETE'])
def delete_a_job(reminder_id):
    a_job = ReminderModel.delete_one(reminder_id)
    return make_response('00201',messages.get('00201').get('en'),results={})