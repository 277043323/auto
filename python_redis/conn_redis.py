from redis import StrictRedis

from rediscluster import *

def main():
    #创建StrictRedis实例链接数据库
    str=StrictRedis(host="",port="")
    # str.set("gg","nn")
    # str.get()

    #redis集群的引用

if __name__=='__main__':
    main()