from redis import StrictRedis
import redis
#redis集群
# from rediscluster import *

def main():
    # 这种连接是连接一次就断了，耗资源.端口默认6379
    #创建StrictRedis实例链接数据库
    # str=StrictRedis(host="192.168.174.134",port="6379")
    str = StrictRedis(host="127.0.0.1",port="6379")
    print(str.set("gg", "nn"))
    print(str.get("gg"))

    # 连接池：
    # 当程序创建数据源实例时，系统会一次性创建多个数据库连接，并把这些数据库连接保存在连接池中，当程序需要进行数据库访问时，
    # 无需重新新建数据库连接，而是从连接池中取出一个空闲的数据库连接
    pool = redis.ConnectionPool(host="127.0.0.1",port="6379")
    r = redis.Redis(connection_pool=pool)



    #redis集群的引用

if __name__=='__main__':
    main()