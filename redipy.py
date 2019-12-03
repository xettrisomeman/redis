import redis


redis_host = "localhost"
redis_port = 6379



def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_port , db=0)

    #set a value
    redisClient.set("name", "someman")

    #set a integer
    redisClient.set("number" ,10)
    

hello_redis()

