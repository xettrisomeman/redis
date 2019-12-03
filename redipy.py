import redis
import time
import datetime


redis_host = "localhost"
redis_port = 6379



def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)

    #set multi key value
    redisClient.mset({"name" : "someman" , "age":20})

    #get multi key (it returns list)
    print(redisClient.mget("name" ,"age"))

    



hello_redis()

