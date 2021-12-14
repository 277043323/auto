# for i in range(10):
#     for j in range(9):
#         print(j,end=' ')
#         # print(i,end=' ')

# 1*1
# 1*2，2*2
#1*3  2*3 3*3
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


#在字典中添加多个数据

dict={
    "name":"你好",
    "age":2,
}
dict.update(
    grade =0,
    sex=1
)
print(dict)