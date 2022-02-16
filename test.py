# for i in range(10):
#     for j in range(9):
#         print(j,end=' ')
#         # print(i,end=' ')

# 1*1
# 1*2，2*2
# 1*3  2*3 3*3
#
# for i in range(1,3):
#     for j in range(1,2):
#         print(str(i)+"*"+str(j),end='')


# lst1 = [1, 3, 5, 7, 8]
# lst2 = [2, 2, 7, 9, 7]
#
# for i in lst1:
#     for j in lst2:
#         if i + j == 10:
#             print(i, j)
#             break


# lst1 = [1, 3, 5, 7, 8]
# lst2 = [2, 2, 7, 9, 7]
#
# for i in lst1:
#     for j in lst2:
#         if i + j == 10:
#             pass
#
#     print(i, j)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i)+"*"+str(j),end=' ')
#     print()

# import hashlib
# a="20211214"
# m =hashlib.md5(a.encode())
# print(m)
# n= hashlib.sha224(a.encode())
# print(n)

# for i in range(1,10):
#     for j in range(1,1+i):
#         print(str(i)+"*"+str(j),end=' ')
#     print()

# for i in range(1,4):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

#
# for i in range(5):
#     for j in range(5-i):
#         print(' ',end=' ')
#     # for k in range(2*i-1):
#     #     print('*',end=' ')
#     print()
# for i in range(3):
#     for j in range(3-i):
#         print(j,end=' ')
#     print()


# for i in range(5):
#     for j in range(i+1):
#         print(' ',end=' ')
#     for k in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(5):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for k in range(2*i-1):
#         print('*',end=' ')
#     print()
# 在字典中添加多个数据
# dict={
#     "name":"你好",
#     "age":2,
# }
# dict.update(
#     grade =0,
#     sex=1
# )
# print(dict)
# 字符串的链接
# r=''
# l=[1,2,3,4,5]
# for i in l:
#     r+=str(i)+'='+str(l[i-1])+'&'
# print(r)
# s ="ssss"
# print(s.lower())
# print(s.upper())
# print(s[::2])
# print(s[:2])
# print(s[:1].replace("s", "v"))
# flag = False
# name = 'luren'
# if name == 'python':         # 判断变量是否为 python
#     flag = True              # 条件成立时设置标志为真
#     print("nihao")    # 并输出欢迎信息
# else:
#     print("error")
# code ="absdd"  #这个值表示的时True
# if not code:   #没有值就打印
#   print("a")
# else:
#   print("error")
#
# #再字符串中拼接一下参数
# url = "https://host%s"%("shi")
# print(url)

# def main(a):
#   if not a:
#     return "testing"
# 更新字符串
# s+='kk'
# print(s)
# print(s[:4] + 'kk')
import re
# str ="<i><color=#CAB1DE>#Welcome to the world of Python</color></i>\n<i><color=#FFFFFF><color=#4BC7FF>for</color>\
#   \ __count <color=#4BC7FF>in</color> <color=#FF7A7A>range</color>(<color=#FFBD45>3</color>):</color></i>\n\
#   \    <i><color=#FFFFFF>codemao.<color=#FFBD45>move</color>()</color></i>\n<i><color=#FFFFFF>codemao.<color=#FFBD45>turnLeft</color>()</color></i>\n\
#   <i><color=#FFFFFF><color=#4BC7FF>for</color> __count <color=#4BC7FF>in</color> <color=#FF7A7A>range</color>(<color=#FFBD45>6</color>):</color></i>\n\
#   \    <i><color=#FFFFFF>codemao.<color=#FFBD45>move</color>()</color></i>\n<i><color=#FFFFFF>codemao.<color=#FFBD45>turnLeft</color>()</color></i>\n\
#   <i><color=#FFFFFF><color=#4BC7FF>for</color> __count <color=#4BC7FF>in</color> <color=#FF7A7A>range</color>(<color=#FFBD45>3</color>):</color></i>\n\
#   \    <i><color=#FFFFFF>codemao.<color=#FFBD45>move</color>()</color></i>\n"
# c="hdhdd"
# k="jjjabc"
# html="<i>hhh</i>k<i></i>"
# if __name__ == '__main__':
#   main("jj")
# 第一个数是开始位置，第二个位置是结束位置，第三个是步长
# print(c[1:3:2])
# print(k[1:2:3])
# p = re.compile('<[^>]+>')
# print(type(p))
# print(p.sub("", str))
# # hh=compile('<>')
# # print(hh.sub("", html))
# print(c[:1])
# print(str[:1])
# hh = re.sub("hd","ghx",c)
# print(hh)
# d =re.compile('[^jjj]')
# print(d.sub("", k))
import sys

from io import BytesIO
import base64

# test_str="yFr4uEdbV0GCj5SJnC5HEGL5M+ECHLS7Ikg9Ld0VW760sPCvTPLdAPam3agEDuHQRUX+mznof/23fECrSprmltS6aAO5hr/hyts8ZVDIrK0kEmDKBH//TfIe8lBsSsT6GBNmpKRku6Y28NCoQa7VrhhP1po2lD6ShuqsSvh76ufnIEciuxfh3p0NIHjOHSJUJwMkMW8j6OMNY12IV44tzZcaNTWgks5w8GLchfd3Oh6SxcY+CrYf8hBVMjG5MA5QbwrNXoAZ5glksqpPOVQtinHATbKPXLm12jyBg452JDFuZotuVHVFL2Ytzk7A1XpWs6SAqoYc7GpQHJ+9BL/kzDNlcLGKNWAg2Of1bLiqf/OxaRE8587AWjVBO6xT9yf9Zp6vJz84ccIHy7VaqmujCtIYrQA/pemIdBLjkl/Gq9fEurd3phl7Nmmmn1JK6BK/oPgPZh26VUvXd+Q9F9I8UbDJ8+KdlFuFhU/hbVeIe0DTObIvUc26pcQ5rMjj1uBG6W5heHGrNcnpuMs3U0sp8y9+UymeZ3Az2Wk2xwWRlFGHw6n9sEJ/6MxLVjZk5sxJ6K0cHy+R2P+aPFAugIw/DHRJGxzUTpv1YeEbcLRMKDXaIaPkDM8VHxI7gVnsBRMgA/ALJi3VfdTGfeU2yGlQcxr0nO8qFljnpUp7ZsAI91lNq40dpyhQTzzDWZA/R5aXtjGn76fL+x2v4kw3MafASp142cfsIuEiOUGS08hiqhsKqJvkj3sJdCRU2fwNc9eYiBNZuaDmSZTSPfURLiF4uzCBycN2C7U+yMnz+goQ6URXvKMs0FnbMWQgBKSsZHX4z6iREVcZr/9NnTZzlRWb9evUnwB7kCNaRCeBhdi5Z8iqKqZMSrBuwa/xp+kGfrJ4iVdpf25PXYEgJoX//tSht68LXv6+MaWLDEfEciN/h7i8JcX3X1DK0RD/O1M42L6TLsGIcnISXDCjebLJoy9Se3UvvBqQ/SkixgkRGwyvASM="
# #解码
# missing_padding = 4-len(test_str)%4
# if missing_padding:
#   test_str+='='* missing_padding
# print(base64.b64decode(test_str))
# #默认以utf8解码
# print(type(base64.b64decode(test_str)))

# base32编码的方式进行编码，出现的字符串：“deviceId: "6a6141c70a48042ff5c8de598ce0d714"”,是否可以看出这个字符串的原始的
# 内容？

# import random
# ms = random.randint(0,999999)
# print(ms)


# 保存登录状态到session中

# 利用flask-session，将session数据保存到redis中

# python
# 用于生成加密信息token
# import secrets
# print(secrets.token_hex())

# web自动化的支持定位元素的几种方法

#
# for i in range(10):
#     print(True)
import yaml
from flask import jsonify
#
# li=[1,2,3,4,5]
#
# li2=[1,2]


# def add(num1,num2):
#     return num1+num2

# 没有return对象默认返回none
# def add(num1,num2):
#     print(num1+num2)
#
# ret = map(add,li,li2)
# # print(type(ret))
#
# for i in ret:
#     print(i)

# from flask import Flask
# app=Flask(__name__)
# #celery
# #定义任务
# @app.route('/',methods=["GET"])
# def main():
#     d={"name":"guo"}
#     param = jsonify(d)
#     print(type(param))
#     return param
#
#
# if __name__=='__main__':
#     app.run()


# 签名，验证过程。
# pytest-xdist  ==可以多任务的执行测试用例
# pytest-assume ==可以执行多个断言
# pytest-html==可生成测试报告
# pytest-rerunfailures
import warnings

import pytest

# def func(x):
#     return x+1
#
# def test_answer():
#     assert func(3)==5

# pytest测试类中不能带__init__()方法？？
# 因为这将阻止类的实例化
# class Test():
#     # def __init__(self):
#     #     self.name="ann"
#     def test_dic(self):
#         # warnings.warn()
#         assert func(3)==4

#
# import pytest
# import smtplib
#
# @pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
# def smtp_connection(request):
#     smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
#     yield smtp_connection
#     print("finalizing {}".format(smtp_connection))
#     smtp_connection.close()
#
# def test03():
#     smtp_connection()
# pytest有个参数执行到一定can'sh

import pytest
# fixture 相当于setup 操作，可是呢，它会相对来所更加的灵活
# 默认的作用域是function

# ---------------------
# autouse使用默认的情况,即autouse=false,手动添加去调用
# def test(login):
#     assert 3==3
# # def test_one():
# #     assert 3==3
# def test_one(login):
#     assert 4==4
#
# def test_two(login):
#     assert 5==5
#
# class Test():
#     def test_three(self,login):
#         assert 6==6
#
#     def test_four(self,login):
#         assert 7==7
#
#
# def test_five():
#     assert 8==8
# -----------------------
# conftest文件中设置autouse=true
# def test():
#     assert 3==3
# # def test_one():
# #     assert 3==3
# def test_one():
#     assert 4==4
#
# def test_two():
#     assert 5==5
#
# class Test():
#     def test_three(self):
#         assert 6==6
#
#     def test_four(self):
#         assert 7==7
#
#
# def test_five():
#     assert 8==8
import pytest

# class Fruit:
#     def __init__(self, name):
#         self.name = name
#         self.cubed = False
#
#     def cube(self):
#         self.cubed = True
#
#
# class FruitSalad:
#     def __init__(self, *fruit_bowl):
#         self.fruit = fruit_bowl
#         self._cube_fruit()
#
#     def _cube_fruit(self):
#         for fruit in self.fruit:
#             fruit.cube()
#
#
# # Arrange
# @pytest.fixture
# def fruit_bowl():
#     return [Fruit("apple"), Fruit("banana")]
#
# def test_fruit_salad(fruit_bowl):
#     # Act
#     fruit_salad = FruitSalad(*fruit_bowl)
#
#     # Assert
#     assert all(fruit.cubed for fruit in fruit_salad.fruit)

# 下列的方式可以枚举出,3个值所有的组合结果
# @pytest.mark.parametrize('a',{"选填","必填"})
# @pytest.mark.parametrize('b',{"选填","必填"})
# @pytest.mark.parametrize('c',{"选填","必填"})
# def test_add(a,b,c):
#     print(a+b+c)
#     return a+b+c
#
# @pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
# def data_set(request):
#     return request.param
#
#
# def test_data(data_set):
#     print(data_set)
#     pass
#
#
# #求多个参数相加的和
# @pytest.fixture(params=[1,2,3,pytest.param(4,marks=pytest.mark.skip)])
# def add(request):
#    return  request.param
#
# def test_data_one(add):
#     print(add + 1)


# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected

# @pytest.mark.parametrize("a,b",[("1+1",2),("2+2",4),("3+3",6)])
# def test_oo(a,b):
#     assert eval(a)==b


# 设置多个断言的情况.只有断言失败后面的断言就不执行了...
# def test():
#     assert 1==1
#     assert 2==0
#     assert 3==3

# ---------多条断言时,所有的断言都会执行的情况
# import pytest
# import pytest_assume
# def test():
#     pytest.assume(3,3)
#     pytest.assume(1,0)
#     pytest.assume(2,2)


# 使用加密后的cookie进入
import requests

# print(sys.path)

# print(yaml.safe_load(open("./data7.yaml", "rb")))
# t = yaml.safe_load(open("./data7.yaml", "rb"))
# l = str(t)
# print(l.replace(' ', '\n'))
# print(t)
# l=''
# e = l + t
# print(e)
# print(e.replace('|', '\n'))
# t.values()
# print(t.keys())
# print(t.values())

# for i in t.keys():
#     print(i)
# print(t)
# print(type(t))

# for i in t.values():
#    l=''
#    e =l + i
#    print(e.replace('|', '\n'))


# p = "ssld"
# f= p.replace('l', '\n')
# print(type(f))
# print(p.replace('l', '\n'))

# print(yaml.safe_load(open("./nn.yaml", "rb")))
#
# t = yaml.safe_load(open("./nn.yaml", "rb"))
# print(type(t))

# 精通

# fixture和yeild组合使用，暂时还不是很能理解。

# nums =[x for x in range(10)]
# print(type(nums))
# print(nums)
#
# #
# num = (x for x in range(5))
# print(num)
# print(type(num))

# def create_num(num):
#     a, b = 0, 1
#     current_num = 0
#     while current_num <=num:
#         print(a)
#         yield a
#         current_num += 1
#         a ,b = b, a+b
#
# print(create_num(5))
# print(next(create_num(5)))

# %专门用于处理字符串中的数据，变量的格式化输出

#
# print("我叫%s"% "小雪")

# 这是一种格式化的写法
# print("我叫{}".format(1))
# name="小雪花"
# # print(f"我叫{name}")
# print("{:.2f}".format(3.1415926))
#
# # 通过字典设置参数
# # site = {"name": "点猫科技", "url": "www.codemao.cn"}
# # print("网站名：{name}, 地址 {url}".format(**site))
#
# student_no=1000001
# print("我的学校是 %05d"% student_no)


# 使用方法名作为参数
# test_user_data = ["tom","jerry"]
# @pytest.fixture(scope="module")
# def login_r(request):
#     user = request.param
#     print(f"登录用户名{user}")
#     return user
#
# # 使其不在某个平台上运行,indirect加了这个参数可以把传入的参数当作函数，不加就不是一个函数了，就是一个变量
# @pytest.mark.skipif(sys.platform=="darwin",reason="不在macos上执行")
# @pytest.mark.parametrize("login_r",test_user_data,indirect=True)
# def test_login(login_r):
#     a =login_r
#     print(a)
#     print(f"测试登录的返回值{a}")
#     assert a != ""

#
# def test_one():
#     print("这是第二个测试用例")
#
#
# def test_two():
#     print("这是第三个测试用例")
#
#
#
# def test_o():
#     print("这是第四个测试用例")
#
#
# def test_t():
#     print("这是第五个测试用例")
#
#
# def test_on():
#     print("这是第六个测试用例")
#
#
# def test_tw():
#     print("这是第七个测试用例")


# 用例之间的前提条件必须，可以使用fixture进行处理
# @pytest.fixture()
# def login_r():
#     print("进行测试之前必须先进行登录操作")
#
# def test_one(login_r):
#     print("这是第一条测试用例")
#
#
# def test_two():
#     print("这条测试用例比较独立，不需要依赖其他的先天的条件")


# 前端自动化中应用-yield
# scope参数module的作用只会在开头可结束的时候调用
# @pytest.fixture(scope="module")
# def open():
#     print("打开浏览器")
#     yield
#     print("执行teardown")
#     print("关闭浏览器")
#
#
# def test_search1(open):
#     print("打印search1")
#     pass
#
# def test_search2(open):
#     print("打印search2")
#     pass
#
# def test_search3(open):
#     print("打印search3")

# scope=module在整个.py文件中都会生效只会被调用一次
#
# @pytest.fixture(scope="session")
# def open():
#     print("打开浏览器")
#     yield "是我啊，这个你知道吗"
#     print("执行teardown")
#     print("关闭浏览器")
#
#
# def test_search1(open):
#     print("打印search1")
#     pass
#
# def test_search2(open):
#     print("打印search2")
#     pass
#
# def test_search3(open):
#     print("打印search3")


# 熟悉装饰器&迭代器并灵活的时候
# @pytest.fixture(scope="module")
# def create_num():
#     a, b = 0, 1
#     current_num = 0
#     print("是我啊，哈哈哈，我看一下这个是怎么回事")
#     while current_num < 4:
#         yield a
#         a, b = b, a+b
#         current_num+=1
#
#
# print(create_num)

# fixture解析模型，具体的规则是怎样的？

# fixture函数是不推荐直接调用的。

# def test_one(create_num):
#
#     pass

# 用协程实现多任务

# import time
# def task_1():
#     while True:
#         print("------1-----")
#         time.sleep(0.1)
#         yield
#
# def task_2():
#     while True:
#         print("------2-----")
#         time.sleep(0.1)
#         yield
#
# # 如下会是先执行第一个任务；再执行第二个任务
# # print(task_1())
# # print(task_2())
#
# #使两个函数一起执行，在函数后加上yield
#
# def main():
#     # 下面是单任务
#     t1 = task_1()
#     t2 = task_2()
#     while True:
#         next(t1)
#         next(t2)
#
# if __name__=="__main__":
#     main()

# def test(a:int):
#     print("函数注释相关声明")
#
#
# # 函数参数的注释是保存在__annotations
# print(test.__annotations__)

# 装饰器的使用。


# 实现一个循环
# i = 0
# if i<=1:
#     print("你好啊")
#     i+=1
#     if i<=2:
#         print("你好啊")
#         i+=1
#         if i<=2:
#             print("你好啊")
#             print(f"i的最终值是{i}")

# j = 0
# while j<=3:
#     print("你好啊")
#     j+=1
#     print("输入j的值%d" %j)


# # 实现0-100的求和
# result = 0
# i =0
# while i <100:
#    # result+=i
#    result+=i
#    i+=1
#    # print(i)
# print(result)
# result = 0
# i =0
# while i <6:
#     if i%2==0:
#         result+=i
#     i+=1
# print(result)
# 求偶数的和
# i=0
# result =0
# while i <100:
#     if i %2 !=0:
#         result+=i
#     i+=1
#     print(i)
# print(result)
# break 当子条件满足时跳出整个循环
# i=0
# result =0
# while i <100:
#     if i ==3:
#         break
#     i+=1
#     print(i)

# continue满足子条件后跳过当前循环，继续下一个循环
# i=0
# result =0
# while i <100:
#     if i ==2:
#         i+=1
#         continue
#     i+=1
#     print(i)

# def function():
#     sum=0
#     i=0
#     while i <100:
#         if i %2 ==0:
#             sum+=i
#         i+=1
#     return sum
#
# print(function())
# i=1
# while i <5:
#     print('*'*i)
#     i+=1

# 一个简单的循环嵌套
# i = 1
# while i <=5:
#     # j=i
#     # while j<i+1:
#     #     print('*')
#     print('*',end='')
#     i+=1


i = 1

# while i <5:
#     j = 1
#     while j <=i:
#         # print("这是列数%d"% j)
#         print("*",end='')
#         j+=1
#     # print("这是第%d行"%i)
#     print("")
#     i+=1
#
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         # print(str(i)+'*'+str(j)+'='+str(i*j),end=" ")
#         # print("%d*%d=%d"% (i,j,i*j),end= ' ')
#         print(f"{i}*{j}={(i * j)}", end=' ')
#         j += 1
#     # print("这是第%d行"%i)
#     print("")
#     i += 1


#
# def main():
#     pass


# print(main.__repr__())
# main._debug__()
# print(type(main))
# print(main.__repr__())
# print(main.__call__())
# i=2
# print(type(i))

# print(main.__call__())
# print(main.__new__())

# 格式化字符串后面的‘()’,本质上就是元组
#
# q
#
# info_tuple = (21.3, "hah", 20)
#
# print("这是我的分数%.2f+这是我的姓名%s+这是我的年龄%d" % info_tuple)
# 列表的使用
# name = "我的名字"
# list=[1,2,3,4,5]
# list.append(6)
# list.remove(2)
# print(list.index(1))
# print(tuple(list))
# del name
# print(list)

dict = {"name": "zhangsan",
        "age": 20, "grade": 123}
#
#
# print(info_tuple)
# print(dict)
#
# import client_socket
#
# print(client_socket.main())
# print("是我的相关数据")

# 字典是无序的，那为什么，输出都是有序的呢？？
# i=1
# while i<100:
#     print(dict)
#     i+=1

# python内置的所有的关键子
# import keyword
#
# print(keyword.kwlist)
#
# print(len(keyword.kwlist))
#
# print(keyword.iskeyword)
import card_tools

# 实现一个名片管理系统
# 由用户主动决定什么时候进行退出
while True:
    # TODO 显示菜单
    # print("选择1表示创建名片")
    # print("选择2表示修改卡片")
    # print("选择3表示删除卡片")
    card_tools.show_meun()
    action_str = input("请输入您的选择:")
    print("您选择的操作是【%s】" % action_str)

    # 选择1，创建账号，2 修改账号信息，3 删除账号，4 退出账号
    # while True:
    # if action_str=='1' or action_str=='2' or action_str=='3'  这个语句与下面的语句一致
    if action_str in ['1', '2', '3']:
        """
        需要做不同选择的处理
        """
        if action_str == '1':
            card_tools.add_card()
        elif action_str == '2':
            card_tools.show_all()
        elif action_str == '3':
            card_tools.find_card()
        # print("您选择的操作是【%s】" % action_str)
    elif action_str == '4':
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("请输入正确的选择")
    # if action_str=='1':
    #     print("创建账号")
    # elif action_str=='2':
    #     print("修改账号信息")
    # elif action_str=='3':
    #     print("删除账号")
    # elif action_str=='4':
    #     print("退出系统")
    # else:
    #     print("请输入正确的数字")
