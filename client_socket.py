import os
import socket
def main():
    #创建socket套接字,,socket是全双工的，可以发送数据也可以同时接收数据。
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #连接服务器
    tcp_socket.connect(('192.168.174.1',7790))
    #打印进程号
    print(os.getpid())
    while True:
        send_data=input("输入你要发送的数据:")
        #发送信息
        tcp_socket.send(send_data.encode('gbk'))
        print(tcp_socket.recv(1024).decode('gbk'))
        #关闭套接字
    tcp_socket.close()
if __name__=='__main__':
    main()