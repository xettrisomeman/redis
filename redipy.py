import redis


redis_host = "localhost"
redis_port = 6379



def hello_redis():

    redisClient = redis.Redis(host=redis_host, port=redis_pord , db=0)

    #set a value
    redisClient.set("name", "someman")

    #get a value

    redisClient.get("name")
    


hello_redis()

