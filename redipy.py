import redis
import time
import datetime


redis_host = "localhost"
redis_port = 6379



def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)

    #set a key
    redisClient.set("country" , "nepal")

    #get len of the string

    print(redisClient.strlen("country"))

    



hello_redis()

