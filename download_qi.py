import socket
def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_socket.connect(('221.5.75.41',443))
    send_data=input("请输入你要下载的文件名称")
    tcp_socket.send(send_data.encode('gbk'))
    file_data = tcp_socket.recv(1024*1024)
    print(file_data)
    with open("testManage.xlsx",'wb') as f:
        f.write(file_data)

    tcp_socket.close()

if __name__=='__main__':
    main()