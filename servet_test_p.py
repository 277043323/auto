
import socket
def Respon_send(new_socket):
    #这里注意window系统换行符是\r\n，不是正斜杠
    response='HTTP/1.1 200 OK \r\n'
    response+='\r\n'
    response+='<h1>大型考试——考试发布</h1>'
    print(new_socket.send(response.encode('gbk')))

def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_socket.bind(('127.0.0.1',8895))
    #128参数制定了内核为此套接口排队的最大连接个数,对于高并发的服务这里这样设置显然是不够的，会比这个大很多。
    tcp_socket.listen(128)
    #链接多个客户端
    new_tcp_socket,addr = tcp_socket.accept()
        #判断客户端请求是否发送完成,这里可以设置程序的内存
    new_tcp_socket.recv(1024*1024).decode('gbk')
    Respon_send(new_tcp_socket)

    new_tcp_socket.close()
    tcp_socket.close()

if __name__ == '__main__':
    main()