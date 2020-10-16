from pymongo import MongoClient

from configs import setting
import datetime
import uuid


class ReminderModel:
    @classmethod
    def connection(cls):
        client = MongoClient(setting.MONGO_HOST, setting.MONGO_PORT)
        db = client[setting.MONGO_DB]
        return db['reminder']
    
    @classmethod
    def add(cls,job_name,address,jobs_id,mobileno,start_date,end_date,description,website_url,resources):
        pass
    
    @classmethod
    def find(cls):
        alljobs = cls.connection().find({},{"_id":0})
        return alljobs if alljobs.count()>0 else []
    
    @classmethod
    def find_one(cls,cusid):
        find_one = cls.connection().find_one({'id':cusid})
        if find_one:
            return find_one
        return {}
        