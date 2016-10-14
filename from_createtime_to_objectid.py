from bson.objectid import ObjectId
import time
import datetime
import sys
objectid=ObjectId(sys.argv[1])
timeStamp = time.mktime(objectid.generation_time.timetuple())
timeArray = time.localtime(timeStamp)
createtime=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print  createtime