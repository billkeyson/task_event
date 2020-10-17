from flask import Blueprint,request
from . import make_response
from models.customer import CustomerModel
from configs.response_message import messages

customer_api = Blueprint("customer_route",__name__,url_prefix="/customer")


@customer_api.route('/add',methods=["POST"])
def add():
    if not request.is_json:
        return make_response('00414',messages.get('00414').get('en'),status=401)
    
    request_response = request.get_json()
    # user_id,name,tags,item_images,category,price,description
    required_fields = ['name','address','mobileno','email']
    for field in required_fields:
        if field not in request_response.keys():
            return make_response('00400',messages.get('00400').get('en'),status=401)
    
    # optional fields
    resources = request_response.get('resources') if request_response.get('resources') else ''
    
    # save jobs to DB
    jobs = CustomerModel.add(request_response.get('name'),request_response.get('mobileno'),request_response.get('email'),request_response.get('address'),resources)
    if jobs:
        return make_response('00200',messages.get('00200').get('en'),results={"uid":jobs},status=200)

@customer_api.route('/')
def find_all():
    all_customer = CustomerModel.find()
    return make_response('00204',messages.get('00204').get('en'),results=all_customer)


@customer_api.route('/<customer_id>')
def find_a_customer(customer_id):
    a_customer = CustomerModel.find_one(customer_id)
    return make_response('00204',messages.get('00204').get('en'),results=a_customer)



@customer_api.route('/<customer_id>',methods = ['DELETE'])
def delte_c(customer_id):
    a_customer = CustomerModel.delete_one(customer_id)
    return make_response('00201',messages.get('00201').get('en'),results={})





