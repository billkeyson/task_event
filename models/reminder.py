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
    def add(cls,start_date,end_date,service_type,interval,jobid):
        reminder  = {}
        reminder['uid'] ='rmd'+datetime.datetime.now().strftime('%Y%m%d') + \
                     uuid.uuid4().urn[11:].replace('-', '').upper()
        reminder['job_id'] = jobid
        reminder['service_type'] = service_type
        reminder['start_date'] = start_date
        reminder['end_date'] = end_date
        reminder['inverval'] = interval
        reminder['start_date'] = start_date
        reminder['atDate']  = datetime.datetime.utcnow()
        reminder['atModified']  = datetime.datetime.utcnow() 
        reminder_response = cls.connection().insert_one(reminder).inserted_id
        if reminder_response:     
            return {
                'uid':reminder['uid'],
                'job_id':reminder['job_id'],
                'service_type':reminder['service_type'],
                'inverval':reminder['inverval'],
                'start_date':str(reminder['start_date']),
                'end_date':str(reminder['end_date']),
                'atDate':str(reminder['atDate']),
                'atModified':str(reminder['atModified'])        
            }  
            
        return False  
    
    @classmethod
    def find(cls):
        allreminder = cls.connection().find({},{"uid":0})
        return allreminder if allreminder.count()>0 else []
    
    @classmethod
    def find_one(cls,reminderid):
        find_one = cls.connection().find_one({'uid':reminderid})
        if find_one:
            return find_one
        return {}
    
    @classmethod
    def delete_one(cls,reminderid):
        find_one = cls.connection().delete_one({'uid':reminderid})
        if find_one:
            return True
        return False
        