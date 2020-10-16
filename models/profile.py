from pymongo import MongoClient
from configs import setting
import datetime
import uuid


class ProfileModel:
    @classmethod
    def connection(cls):
        client = MongoClient(setting.MONGO_HOST, setting.MONGO_PORT)
        db = client[setting.MONGO_DB]
        return db['project']
    
    
    @classmethod
    def add(cls,username,email,password):
        uid = 'uid'+datetime.datetime.now().strftime('%Y%m%d') + \
                     uuid.uuid4().urn[9:].replace('-', '').upper()
        add  = cls.connection().insert_one({'uid':uid,"username":username,"email":email,"password":password})
        return True if add else False
    
    @classmethod
    def login(cls,email,password):
       login =  cls.connection().find_one({'email':email,'password':password},{'_id':0,'email':1,'phone_number':1,'username':1})
       return login if login else {}
       