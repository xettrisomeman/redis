import redis
import time
import datetime


redis_host = "localhost"
redis_port = 6379


#HASHMAP

def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)


    #pop value from top
    redisClient.lpop("numbers")



    #pop value from bottom
    redisClient.rpop("numbers")

    print(redisClient.lrange("numbers" , 0,-1))



hello_redis()

