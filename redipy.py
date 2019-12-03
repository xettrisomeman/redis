import redis
import time
import datetime


redis_host = "localhost"
redis_port = 6379


#HASHMAP

def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)



    #create a set
    #sadd(keyname,value,value) we can add as much as value we need
    #set is created value in random
    redisClient.sadd("hello" , 1,2,3,4)

    #get a set
    print(redisClient.smembers("hello"))


    # NOTICE: set cannot have duplicates value


hello_redis()

