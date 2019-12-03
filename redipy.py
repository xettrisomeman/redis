import redis
import time
import datetime


redis_host = "localhost"
redis_port = 6379


#HASHMAP

def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)



    #get len of set

    print(redisClient.scard("hello"))


    # NOTICE: set cannot have duplicates value


hello_redis()

