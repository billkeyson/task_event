from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient
from configs import setting
from . import socketio,make_response

# def tick():
#     f =  open("names.txt",'a')
#     f.write("Hell \n")
#     f.close()
#     print('Tick! The time is: ')
class SchedulerCron:
    @classmethod
    def connection(cls):
        client = MongoClient(setting.MONGO_HOST, setting.MONGO_PORT)
        db = client[setting.MONGO_DB]
        return db['reminder']
    
    @classmethod
    def checkRminder(cls,interval):
        _inter = cls.connection().find({'interval':interval},{"_id":0})
        if _inter.count()>0:
            intervals = []
            for i in _inter:
                i['atDate'] = str(i['atDate'])
                i['atModified'] = str(i['atModified'])
                intervals.append(i)
            socketio.emit("reminder_interval",{"code":"interval minute {}".format(interval),"result":intervals})
            # print("",intervals)
            
            
    @classmethod
    def secondsMinute(cls):
        cls.checkRminder(10)
    
    @classmethod
    def seconds3Minute(cls):
        print("4 seconds")
        # cls.checkRminder(10)
        
    @classmethod
    def TenMinute(cls):
        cls.checkRminder(10)
    
    @classmethod
    def TwentyMinute(cls):
        cls.checkRminder(20)

    
    @classmethod
    def TirtyMinute(cls):
        cls.checkRminder(30)
    
    @classmethod
    def FortyMinute(cls):
        cls.checkRminder(40)
    @classmethod
    def FiftyMinute(cls):
        cls.checkRminder(50)
    
    @classmethod
    def SixtyMinute(cls):
        cls.checkRminder(60)
    
    @classmethod
    def SeventyMinute(cls):
        cls.checkRminder(70)
    
    @classmethod
    def EightyMinute(cls):
        cls.checkRminder(80)
    
    @classmethod
    def NintyMinute(cls):
        cls.checkRminder(90)
    
    @classmethod
    def run(cls):
        scheduler = BackgroundScheduler(daemon=True)  
        # scheduler.add_job(cls.secondsMinute, 'interval', seconds =40)
        # scheduler.add_job(cls.seconds3Minute, 'interval', seconds =10)
        scheduler.add_job(cls.TenMinute, 'interval', minutes =10)
        scheduler.add_job(cls.TwentyMinute, 'interval', minutes =20)
        scheduler.add_job(cls.TirtyMinute, 'interval', minutes =30)
        scheduler.add_job(cls.FortyMinute, 'interval', minutes =40)
        scheduler.add_job(cls.FiftyMinute, 'interval', minutes =50)
        scheduler.add_job(cls.SixtyMinute, 'interval', hours =1)
        scheduler.add_job(cls.SeventyMinute, 'interval', hours =1,minutes=10)
        scheduler.add_job(cls.EightyMinute, 'interval', hours =1,minutes=20)
        scheduler.add_job(cls.NintyMinute, 'interval', hours =1,minutes=30)
        scheduler.start()
        
