import io
# #定义一个变量
# #当字符串修改比较频繁的时候可以考虑使用这个
# s ="hello the world "
# #生成一个可变的对象
# si = io.StringIO(s)
# print(si)
# si.seek(7)
# print(si.write("kaokao"))
# print(si.getvalue())
# print(si)
# si.seek(9)
# si.write("kk")
# print(si.getvalue())

#判断一个对象是否是可迭代的对象
# from collections import Iterable
#
# print(isinstance(1, Iterable))
#
# print(type(Iterable))
#
# #对象有3个属性 id ,type,value
#迭代器
# class Test():
#     def __init__(self,obj):
#         self.obj=obj
#         self.num=0
#     #迭代器
#     def __iter__(self):
#         pass
#     def __next__(self):
#         if self.num<len(self.obj.name):
#             ret = self.obj.name[self.num]
#             self.num+=1
#             return ret
#         else:
#             raise StopIteration
#
# # t=Test()
#
# #创建一个可迭代的对象
# from collections import Iterable
# from collections import Iterator
# class T():
#     def __init__(self):
#      self.name = list()
#     #返回了一个迭代器
#     def __iter__(self):
#         return Test(self)
#
#     def names(self,age):
#         self.name.append(age)
#
# LL=T()
# LL.names("aa")
# LL.names("bb")
# LL.names("cc")
#
# # print(isinstance(LL, Iterable))
# # #可迭代对象转可迭代器
# # iter(LL)
# # print(isinstance(iter(LL), Iterator))
# # print(next(iter(LL)))
#
# for temp in LL:
#     print(temp)

# class Test_Iter(object):
#     def __init__(self):
#         self.name=list()
#         self.num=0
#     #类中有这个函数，那么实例化的对象就可迭代
#     def __iter__(self):
#         return self
#
#     #类中有这个函数那么就可以获取对象中的值
#     def __next__(self):
#         if self.num<len(self.name):
#             ret = self.name[self.num]
#             self.num+=1
#             return ret
#         else:
#             raise StopIteration
#
#     def names(self,age):
#         self.name.append(age)
#
#
# TT=Test_Iter()
# TT.names("小小")
# TT.names("好好")
# from collections import Iterable
#
# print(isinstance(TT, Iterable))
#
# for temp in TT:
#     print(temp)
#
#
# def fabiaaii(n):
#     n=0
#     a=0
#     b=1
#     while n<10:
#         yield a
#         a,b = b,a+b
#         n+=1
#
# for item in fabiaaii(10):
#     print(item)


# import selenium
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# driver.get("https://test-boat.codemao.cn/testSiteExam/list")

# 进程切换需要更多的内存空间
# import time
#
#
# def task_1():
#     print("-------1--------")
#     time.sleep(0.1)
#     yield
#
#
# def task_2():
#     print("--------2--------")
#     time.sleep(0.1)
#     yield
#
#
# def main():
#     t1 = task_1()
#     t2 = task_2()
#     while True:
#         next(t1)
#         next(t2)
# if __name__=='__main__':
#     main()

import urllib.request


import requests
class DownLoad():
    #下载第一章
    def test_one(self):
        ret  = urllib.request.urlopen("https://static.codemao.cn/new_question/S1xjQQNT0d")
        print(type(ret))
        content_text = ret.read()
        with open("2.jpg","wb") as f:
            f.write(content_text)
    #下载第二章
    def test_two(self):
        pass

#
# ret = requests.get(url="https://static.codemao.cn/new_question/S1xjQQNT0d")
# print(type(ret))
# print(ret.json())

#下载下说

