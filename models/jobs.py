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
    def add(cls,job_name,address,mobileno,start_date,end_date,description,website_url,resources,client_id):
        jobs={}
        jobs['uid'] ='job'+datetime.datetime.now().strftime('%Y%m%d') + \
                     uuid.uuid4().urn[9:].replace('-', '').upper()
        jobs['client_id']  = description
        jobs['job_name'] =job_name
        jobs['address'] = address
        jobs['mobileno'] =mobileno
        jobs['start_date'] = start_date
        jobs['end_date']  = end_date
        jobs['description']  = description
        jobs['website_url']  = website_url
        jobs['resources']  = resources  
        jobs['status']  = 0  
        jobs['atDate']  = datetime.datetime.utcnow()
        jobs['atModified']  = datetime.datetime.utcnow()
        jobsid = cls.connection().insert_one(jobs).inserted_id
        return jobs['uid'] if jobsid else False
    
    @classmethod
    def find(cls):
        alljobs = cls.connection().find({},{"_id":0})
        all = []
        if alljobs.count()>0:
            for job in alljobs:
                job['atDate'] = str(job['atDate'])
                job['atModified'] = str(job['atModified'])
                all.append(job)
            return  all
        return []
    
    @classmethod
    def find_one(cls,jobid):
        find_one = cls.connection().find_one({'uid':jobid})
        if find_one:
            find_one.pop("_id")
            find_one['atDate'] = str(find_one['atDate'])
            find_one['atModified'] = str(find_one['atModified'])
            return find_one
        return {}
        
    
    @classmethod
    def delete_one(cls,jobid):
        find_one = cls.connection().delete_one({'uid':jobid})
        return True if find_one else False
