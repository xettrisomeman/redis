import redis
import time
import datetime


redis_host = "localhost"
redis_port = 6379


#HASHMAP

def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)


    #get a legth of a list
    print(redisClient.llen("numbers"))
    


hello_redis()

