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

    #delete a key
    redisClient.hdel("stud:101" , "age")


    print(redisClient.hgetall("stud:101"))
hello_redis()

