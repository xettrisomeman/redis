import redis
import time
import datetime


redis_host = "localhost"
redis_port = 6379



def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)

    #set a value for a expiry date
    date = datetime.timedelta(seconds=10)

    #set a value for 10 seconds
    redisClient.setex("name" , date,value="someman")

    #print
    print(redisClient.get("name"))
    #wait for 10 seconds
    time.sleep(10)
    #again do the printing
    print(redisClient.get("name"))

    



hello_redis()

