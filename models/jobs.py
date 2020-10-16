from pymongo import MongoClient

from configs import setting
import datetime
import uuid


class JobsModel:
    @classmethod
    def connection(cls):
        client = MongoClient(setting.MONGO_HOST, setting.MONGO_PORT)
        db = client[setting.MONGO_DB]
        return db['jobs']
    
    @classmethod
    def add(cls,job_name,address,mobileno,start_date,end_date,description,website_url,resources):
        jobs={}
        jobs['uid'] ='job'+datetime.datetime.now().strftime('%Y%m%d') + \
                     uuid.uuid4().urn[9:].replace('-', '').upper()
        jobs['job_name'] =job_name
        jobs['address'] = address
        jobs['mobileno'] =mobileno
        jobs['start_date'] = start_date
        jobs['end_date']  = end_date
        jobs['description']  = description
        jobs['website_url']  = website_url
        jobs['resources']  = description  
        jobs['atDate']  = datetime.datetime.utcnow()
        jobs['atModified']  = datetime.datetime.utcnow()
        jobsid = cls.connection().insert_one(jobs).inserted_id
        return jobs['uid'] if jobsid else False
    
    @classmethod
    def find(cls):
        alljobs = cls.connection().find({},{"_id":0})
        return alljobs if alljobs.count()>0 else []
    
    @classmethod
    def find_one(cls,cusid):
        find_one = cls.connection().find_one({'id':cusid})
        if find_one:
            find_one['atDate'] = str(find_one['atDate'])
            find_one['atModified'] = str(find_one['atModified'])
            return find_one
        return {}
        