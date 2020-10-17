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
        allreminder = cls.connection().find({},{"_id":0})
        reminders = []
        for reminder in allreminder:
            reminder['atDate'] =str(reminder['atDate'])
            reminder['atModified'] =str(reminder['atModified'])
            reminders.append(reminder)
        return reminders
    
    @classmethod
    def find_one(cls,reminderid):
        find_one = cls.connection().find_one({'uid':reminderid})
        if find_one:
            find_one.pop("_id")
            find_one['atDate'] = str(find_one['atDate'])
            find_one['atModified'] = str(find_one['atModified'])
        return {}
    
    @classmethod
    def delete_one(cls,reminderid):
        find_one = cls.connection().delete_one({'uid':reminderid})
        if find_one:
            return True
        return False
        