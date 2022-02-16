# s="ss"
# c = list(s)
# print(c)
# d = str(c)
# print(d.count)
# print(s.count(s))

#
# # a={1,2,2,2,3,3,4,4}
# a="{1,2,2,2,3,3,4,4}"
# print(a.count(str(2)))

# b = list(a)
# print(a)

# print(a[2])

# list=[1,2,3,4,2]
# # print(list.count(2))
# for i in list:
#     if i ==2:
#         print("你好啊")
#         # break
# else:
#     print("很抱歉没有找到你的名字")


# num = 10
#
#
# def test1():
#     print("输入的变量是%d" % num)
#
#
# def test2():
#     print("这是输入的第二个%d" % num)
# # 在这个地方设置一个断点，所谓断点就是程序运行的时候，到这个地方时停止继续运行，会出现一个蓝色的选中标记，若程序运行过程中出错是无法到达这里的。
# test1()
# test2()

# 设置全局变量
# num = 10
#
#
# def test():
#     num = 99
#     print("test打印的值时%d"% num)
#
#
# def test_2():
#     print("test2打印的值是%d"% num)
#
#
# test()
# test_2()


# 修改全局变量
# num = 10
#
# def test():
#     # global 改变全局变量可用的关键字
#     global num
#     num = 99
#     print("test打印的值时%d"% num)
#
#
# def test_2():
#     print("test2打印的值是%d"% num)
#
#
# test()
# test_2()
# 列表赋值相关
# 可变的全局变量， 不可变的全局变量
# num_list = [1, 2, 3, 4]
#
#
# def test():
#     num_list.append(5)
#     print("输出的变量列表是%s"% num_list)
#
#
# test()
# 可变的全局变量
# num_list = [1, 2, 3, 4]
# print(id(num_list))
#
#
# def test():
#     # 函数内部修改列表的值，不会生产新的变量
#     num_list.append(5)
#     print("输出的变量列表是%s" % num_list)
#     return num_list
#
#
# mm = test()
# print(id(mm))

# +=，大多数情况执行的是赋值操作，在函数内对变量进行赋值操作会生产新的变量
# 但对列表变量进行+=操作,实际进行的操作是extend(),操作。没有生产新的变量

# num_list = [1,2,3,4]
# print(id(num_list))
#
#
# def test(num_list):
#     # num_list+=num_list
#     num_list=num_list+num_list
#     print(num_list)
#     print(id(num_list))
#
#
# test(num_list)
# print(num_list)


# num="ssd"
#
# print(id(num))
#
#
# def test():
#     print(num.count('s'))
#
#
#
# mm = test()
# print(mm)
# print(id(mm))


# nn="ddd"
# print(id(nn))

# 修改可变的数据类型，修改前后，是同一个对象
# dict={"ss":"f","name":"ghx"}
# print(id(dict))
# print(dict.pop('name'))
# print(dict.clear())
#
# print(dict)
# print(id(dict))

# 修改不可变数据类型，修改前后是同一个对象
# num="we"
# print(id(num))
# print(num.upper())
# print(id(num))

# 赋值操作后对象改变
# num=10
# print(num)
# print(id(num))
# num+=1
# print(num)
# print(id(num))


# str="eee"
# print(str)
# print(id(str))
# # print('-'.join(str))
# str+=str
# print(str)
# print(id(str))

# num=10
#
# def test():
#     pass


# def test(num,*args,**kwargs):
#     print(num)
#     print(args)
#     print(kwargs)
#
#
# # test(1)
# test(1,3,4,5,name="小明")
# test({"ss":"sss","ssh":"ssss"})

# t = input("请输入你的值")
# print(type(t))


# def test(num):
#     if num == 1:
#         return num
#     return num + test(num - 1)
#
#
# sum = test(100)
# print(sum)

# def test(num):
#     if num == 1:
#         return num
#     return num + test(num - 1)
#
#
# sum = test(100)
# print(sum)
# 输出7位数的递归数列
# 0
# 1
# 1
# 2
# 3 num-2
# 5 num-1
# 8 num = (num-2)+(num-1)


# def test(num):
#     # print(num)
#     if num <= 1:
#         return num
#     return test(num - 1)+test(num-2)
#
#
# print(test(3))


# print(test)

# 0+....+100
# sum =0
# i=0
# while i<=100:
#     print(i)
#     sum+=i
#     i+=1
#
#
# print("0-100之前的和%d"% sum)
# input_num = int(input("请输入你想输入多少个数"))
# if input_num<0:
#     print("请输入整数 ")
# else:
#     for i in range(input_num):
#         print(test(i))
# # 成员运算符 in not in
# def recursion(depth):
#     depth+=1
#     print(depth)
#     recursion(depth)
#
# recursion(0)
#
# def test(num):
#     print(num)
#     if num<=1:
#         return num
#     else:
#         return test(num-2)+test(num-1)
#
#
# print(test(4))

# 静态方法

# 类方法

# 对象方法
# 设置一个全局的变量
# kkko = 1
#
#
# class Demo_Test(object):
#     num = 10
#     _inoo = None
#
#     def __init__(self, name, inoo: int = None):
#         print(self)
#         self.name = name
#         self.age = 18
#         self.sex = None
#         if inoo is None:
#             self._inoo = "https://test-boat.codemao.cn"
#         else:
#             print("你可以自己传一个值啊")
#
#     @classmethod
#     def input_data(cls):
#         print(cls)
#         cls.num = 100
#         print(cls.num)
#
#     def send_message(self):
#         print(self.name)
#
#     @staticmethod
#     def get_message():
#         print("游戏相关的文档声明")


# print(Demo_Test)
# nihao = Demo_Test("cat")
# nihao.send_message()
# # print(nihao)
# # nihao.send_message()
# nihao.input_data()
# nihao.get_message()

# nihh = Demo_Test()
# print(nihh)
# nihh.send_message()
# nihao.send_message()

#
# class xiaoxiao(Demo_Test):
#
#     def nihao(self):
#         print(self)
#         print(self.name)
#         print()
#
#     # 使用类的方法可以调用类的属性
#     @classmethod
#     def nn(cls):
#         cls.num = 100
#         print(cls.num)
#
#     @staticmethod
#     def kkl():
#         global kkko
#         kkko = 100
#         print(kkko)
#         print(id(kkko))
#
#
# # kaokao = xiaoxiao("nihaoa", inoo="nihao")  # 实例化对象创建一个对象的内存空间，2初始化对象属性
# #
# # # kaokao.nihao()
# # # kaokao.nn()
# # print(kaokao.kkl())
# # print(kkko)
# # print(id(kkko))
#
# class test_kk_pp(xiaoxiao):
#     # 重写对象的属性方法，super(),调用父类的方法
#     def __init__(self):
#         # 调用父类的属性
#         super().__init__("nn")
#         self.kk = "这是要干啥子"
#
#     def hh(self):
#         print(self.kk)
#         print(self.age)
#
#
# kka = test_kk_pp()
# # print(kka.kk)
# kka.hh()

# 单类模式设计
# 所有的类默认都是继承object类的,只是在python3中可写出来也可以不写.有时候会忘记写出来.

# class Student_NO(object):
#     #我在这里重写了__new__方法.
#     def __new__(cls, *args, **kwargs):
#         new = super().__new__(cls)
#         print(new)   #__new__函数会在实例化对象的时候给对象分配内存空间,返回对象的引用
#         return new
#     # 然后在执行__init__方法,给对象执行初始化的操作
#     def __init__(self,name):
#         self.name=name
#         self.age=18
#
#     def test01(self):
#         pass
#
# print(Student_NO("是我"))
# print(Student_NO.__name__)
# print(Student_NO.__repr__)
# print(Student_NO())
# hh = Student_NO()
# print(hh)
# nn= Student_NO()
# print(nn)


# class PO_K(object):
#     def __init__(self):
#         self.name="hah"

def test_oo():
    print("这个数据很好啊")


def test():
    print("你好啊")


# print(test_oo.__dir__())
# #
# # print(test.__name__("hh"))
# print(__name__)
# # print(test_oo.__name__)
#
# if __name__=='__main__':
#     test()

# __all__=["kkkkkkkk"]
#
# 使用__all__这个属性,可以控制对外暴露的的变量.没有写,那么就算外面的文件有导入这个模块(注意是以*发方式的导入),但任然无法使用这个模块中定义的变量
# __all__=[]
# 实现单类模型
# 封装一个类
# 模块的导入实际上就是导入了__init__.py文件
# import flask_learn
kkkkkkkk="dd"
class Demo_Test():
    LL = None
    name= "这是一个单类设计模型"

    def __new__(cls, *args, **kwargs):
        print(cls.LL)
        if cls.LL is None:
            oK = super().__new__(cls)
            cls.LL=oK
            return oK
        return cls.LL

    def __init__(self, role_id):
        self.role_id = role_id

    def test(self):
        print("实现单类模型%s" % self.role_id)

    @classmethod
    def test_one(cls):
        print(cls.name)


    @staticmethod
    def test_two():
        print(__name__)

        print("你好啊")

DD = Demo_Test("123")
if __name__=='__name__':
    # 实例化多个对象
    print(DD)
    print(DD.test())
    # KL = Demo_Test("234")
    # print(KL)
    # DD.test_two()
    #

# print(__name__)