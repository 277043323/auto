import multiprocessing

# #创建一个q对象作为内存
# q = multiprocessing.Queue(3)
# print(q)
# #向q对象中放入数据
# #没有内存的时候再写入，也会一直等着，即阻塞
# q.put('nihao')
# q.put([1,2,4])
# q.put({'name':'hello'})
# #数据取完之后，之后会一直等着，即阻塞
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())


def download(q):
    ls_data=[1,2,3,4]
    for temp in ls_data:
        q.put(temp)
    print("数据下载完成")

def anay_data(q):
    s=list()
    while True:
        q.get()
        if q.empty():
            break
    print("数据下载成功")


def main():
    q = multiprocessing.Queue(4)
    multiprocessing.Process(target=download,args=(q,))
    multiprocessing.Process(target=anay_data,args=(q,))


if __name__=='__main__':
    main()