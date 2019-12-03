import redis
import time
import datetime


redis_host = "localhost"
redis_port = 6379


#HASHMAP

def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)

    #set a hash key
    hash_set = {"name" : "someman" , "age" : 10 , "country": "Nepal"}

    redisClient.hmset("stud:101" , hash_set)


    #get list of keys
    print(redisClient.hkeys("stud:101"))

    #get list of values
    print(redisClient.hvals("stud:101"))



hello_redis()

