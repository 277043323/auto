#!coding=utf-8
#udp发送数据,
import socket
# def main():
#     #创建一个socket套接字对象
#     udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     #发送信息给目标地址
#     while True:
#         send_data=input("请输入你要发送的数据")
#         # udp_socket.sendto(b"hahaha",("192.168.174.1",8081))
#         #这里如果使用utf-8进行编码的话，接收端如果不试用一致的解码就会出现乱码
#         # udp_socket.sendto(send_data.encode("utf-8"), ("192.168.174.1", 8081))
#         #window系统默认使用的编码格式就是gbk
#         udp_socket.sendto(send_data.encode("gbk"), ("192.168.174.1", 8081))
#     #关闭套接字
#     udp_socket.close()
#
# if __name__=='__main__':
#     main()

#udp接收数据
# import socket
# def main():
#     #创建一个套接字
#     udp_accer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     #绑定一个端口
#     addr = udp_accer.bind(('',7788))
#     #接口数据，多行缩进选中要缩进的段落按Tab键即可
#     while True:
#         recv_data = udp_accer.recvfrom(1024)
#         # print(recv_data)
#         recv_msg = recv_data[0]
#         #解码,win默认的编码格式是gbk
#         print("%s"% recv_msg.decode("gbk"))
# #关闭套接字
#     udp_accer.close()
# if __name__=='__main__':
#     main()

 #UDP发送信息,不安全，不管信息有没有成功发送到服务端，这里只管发送信息

# import socket
# def main():
#     #创建套接字
#     tcp_msg=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     #发送信息
#     tcp_msg.sendto(b'kkkk',("192.168.174.1",8082))
#     #关闭套接字
#     tcp_msg.close()
#
# if __name__=='__main__':
#     main()
#udp聊天器
# import socket
# def main():
#     udp_accept=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
#     udp_hh = udp_accept.bind(('',7788))
#     #shift+Tab缩进向左
#     while True:
#         udp_data=udp_accept.recvfrom(1024)
#         # print(udp_data)
#         udp_msg = udp_data[0]
#         print("%s"%udp_msg.decode('gbk'))
#         send_data = input("请输入你发送的数据：")
#         udp_accept.sendto(send_data.encode('gbk'), ('192.168.174.1', 8081))
#     udp_accept.close()
# if __name__=='__main__':
#     main()

#TCP客户端
# import socket
# def main():
#     #创建socket套接字
#     tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     #连接服务器
#     tcp_socket.connect(('192.168.174.1',8082))
#     send_data=input("输入你要发送的数据:")
#     #发送信息
#     tcp_socket.send(send_data.encode('gbk'))
#     #关闭套接字
#     tcp_socket.close()
# if __name__=='__main__':
#     main()
#TCP服务端,TCP相比与UDP是安全的，客户端要要连接服务端-建立连接的过程
#socket是双全工，可以收信息也可以发信息
import socket
def main():
    #创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定一个ip和端口
    tcp_socket.bind(('', 7790))
    #监听客户端发送信息
    tcp_socket.listen(128)
    #等待客户端的连接
    while True:
        new_tcp_socket,client_addr = tcp_socket.accept()
        print(new_tcp_socket)
        print(client_addr)

#接收客户端发来的信息（备注：这里要注意服务端都是先接收信息的）
        while True:
            accp_data= new_tcp_socket.recv(1024)
            print(accp_data.decode('gbk'))
            send_data=input("请输入你要发送的信息:")
            #回送一部分信息给客户端
            if accp_data:
                new_tcp_socket.send(send_data.encode('gbk'))
            else:
                break
        #接收信息
        new_tcp_socket.close()
    tcp_socket.close()

if __name__=='__main__':
    main()



