import socket
def main():
    #创建socket套接字,,socket是全双工的，可以发送数据也可以同时接收数据。
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #连接服务器
    tcp_socket.connect(('192.168.174.1',7790))
    while True:
        send_data=input("输入你要发送的数据:")
        #发送信息
        tcp_socket.send(send_data.encode('gbk'))
        #recv(1024)这表示的是接收1024位字节1024*1024表示接收1K的数据byte类型就是二进制。
        print(tcp_socket.recv(1024).decode('gbk'))
        #关闭套接字
    tcp_socket.close()
if __name__=='__main__':
    main()