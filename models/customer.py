from pymongo import MongoClient

from configs import setting
import datetime
import uuid


class CustomerModel:
    @classmethod
    def connection(cls):
        client = MongoClient(setting.MONGO_HOST, setting.MONGO_PORT)
        db = client[setting.MONGO_DB]
        return db['customer']
    
    @classmethod
    def add(cls,name,mobileno,email,address,resource):
        customer={}
        customer['uid'] ='cus'+datetime.datetime.now().strftime('%Y%m%d') + \
                     uuid.uuid4().urn[9:].replace('-', '').upper()
        customer['fullname'] =name
        customer['address'] = address
        customer['mobileno'] =mobileno
        customer['email'] = email
        customer['resource']  = resource
        customer['atDate']  = datetime.datetime.utcnow()
        customer['atModified']  = datetime.datetime.utcnow()
        
        
        customerid = cls.connection().insert_one(customer).inserted_id
        return customer['uid'] if customerid else False
    
    @classmethod
    def find(cls):
        allcustomer = cls.connection().find({},{"_id":0})
        return list(allcustomer )if allcustomer.count()>0 else []
    
    @classmethod
    def find_one(cls,cusid):
        find_one = cls.connection().find_one({'uid':cusid})
        if find_one:
            find_one.pop("_id")
            find_one['atDate'] = str(find_one['atDate'])
            find_one['atModified'] = str(find_one['atModified'])
            
            return find_one
        return {}
    
    @classmethod
    def delete_one(cls,cusid):
        find_one = cls.connection().delete_one({'uid':cusid})
        if find_one:
            return True
        return False
        