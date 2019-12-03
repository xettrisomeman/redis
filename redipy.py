import redis
import time
import datetime


redis_host = "localhost"
redis_port = 6379


#HASHMAP

def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)



    #get value from index

    #lindex(key , index)

    #get first element of the list
    print(redisClient.lindex("numbers" , 0))



hello_redis()

