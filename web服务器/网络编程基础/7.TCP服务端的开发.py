"""
1.开发TCP服务端程序开发步骤
1.1 创建服务端套接字对象
1.2 绑定端口号
1.3 设置监听
1.4 等待接受客户端的连接请求
1.5 接收数据
1.6 发送数据
1.7 关闭套接字

2.socket类的介绍
导入socket模块
import socket
创建服务端socket对象
socket.socket(AddressFamily,Type)
方法说明：
1.bind(host,port)表示绑定端口号，host是ip地址，port是端口号，ip地址一般不指定，表示本机的任何一个ip地址都可以
2.listen(backlog)表示设置监听，backlog参数表示最大等待建立连接的个数
3.accept()表示等待接受客户端的连接请求
4.send(data)表示发送数据，data是二进制数据
5.recv(buffersize)表示接收数据，buffersize是每次接收数据的长度

说明：
当客户端和服务端建立连接后，服务端程序退出后端口号不会立即释放，需要等待大概1-2分钟
解决方法有两种：
1.更换服务端端口号
2.设置端口号复用（推荐），就是让服务端程序推出后端口号立即释放

代码如下：

"""

import socket

if __name__ == '__main__':

    # 1.1 创建服务端套接字对象
    # AF_INET:ipv4,AF_INET:ipv6
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口号复用，表示意思：服务端程序退出端口号立即释放
    # 1. SOL_SOCKET: 表示当前套接字
    # 2. SO_REUSEADDR: 表示复用端口号的选项
    # 3. True：确定复用
    #1.2 绑定端口号
    # 第一个参数表示ip地址，一般不用指定，表示本机的任何一个ip即可
    # 第二个参数表示端口号
    tcp_server_socket.bind('',9090)
    #1.3 设置监听
    # 128:表示最大等待建立连接的个数
    tcp_server_socket.listen(128)
    #1.4 等待接受客户端的连接请求
    # 注意点：每次当客户端和服务端建立连接成功都会返回一个新的套接字
    # tcp_server_socket只负责等待接收客户端的连接请求，收发消息不适用该套接字
    new_client,ip_port = tcp_server_socket.accept()
    # 代码执行到此，说明客户端和服务端建立连接成功
    print('客户端的ip和端口号为：',ip_port)
    #1.5 接收数据
    # 收发消息都使用返回的这个新的套接字
    recv_data = new_client.recv(1024)
    # 对二进制数据进行解码变成字符串
    recv_content = recv_data.decode('gbk')
    print('接收客户端的数据为：',recv_content)
    #1.6 发送数据
    send_content = '问题正在处理中...'
    # 对字符串进行编码
    send_data = send_content.encode('gbk')
    new_client.send(send_data)
    # 关闭服务端与客户端套接字，表示和客户端终止通信
    #1.7 关闭套接字，表示服务端一行不再等待接受客户端的连接请求
    tcp_server_socket.close()
