import redis
import time
import datetime


redis_host = "localhost"
redis_port = 6379


#HASHMAP

def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)


    #push from bottom to a list

    #first get a keys
    print(redisClient.keys('*'))

    #check if the key is list or not
    print(redisClient.type("numbers"))

    #push 1 from bottom
    redisClient.rpush("numbers",1)
    print(redisClient.lrange("numbers" , 0,-1))


hello_redis()

