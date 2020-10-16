from flask import Blueprint,request
from . import make_response
from models.jobs import JobsModel
from configs.response_message import messages

job_api = Blueprint("job_route",__name__,url_prefix="/job")


@job_api.route('/add',methods=["POST"])
def add():
    if not request.is_json:
        return make_response('0401','Error: json header',status=401)
    request_response = request.get_json()
    # job_name,address,jobs_id,mobileno,start_date,end_date,description,website_url,resources
    required_fields = ['job_name','address','mobileno','start_date','description']
    for field in required_fields:
        if field not in request_response.keys():
            return make_response('00300',messages.get('00300').get('en'),status=401)
    
    # optional fields
    website_url=  request_response.get('website_url') if request_response.get('website_url') else ''
    end_date=  request_response.get('end_date') if request_response.get('end_date') else ''
    resources = request_response.get('resources') if request_response.get('resources') else ''
    
    # save jobs to DB
    jobs = JobsModel.add(request_response.get('job_name'),request_response.get('address'),\
        request_response.get('mobileno'),request_response.get('start_Date'),\
            end_date,request_response.get('description'),website_url,resources)
    if jobs:
        return make_response('00200',messages.get('00200').get('en'),results={"uid":jobs},status=200)
    return make_response('00422',messages.get('00422').get('en'),results={"uid":jobs},status=401)

@job_api.route('/all')
def find_all():
    all_customer = JobsModel.find()
    return make_response('00204',messages.get('00422').get('en'),results=all_customer)


@job_api.route('/<job_id>')
def find_a_job(job_id):
    a_job = JobsModel.find_one(job_id)
    return make_response('00204',messages.get('00422').get('en'),results=a_job)



@job_api.route('/<job_id>',methods = ['DELETE'])
def delete_a_job(job_id):
    a_job = JobsModel.find_one(job_id)
    return make_response('','',results=a_job)