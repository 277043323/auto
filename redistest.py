import redis

r = redis.StrictRedis(host="127.0.0.1",port=6379,db=0,decode_responses=True)
r.set("guoguo","hello redis")
print(r.get("guoguo"))