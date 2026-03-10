"""
1.静态web服务器的问题
目前的web服务器，不能支持多用户同时访问，只能一个一个的处理客户端的请求，可以使用多线程开发多任务
版的web服务器同时处理多个客户端的请求且比进程更加节省内存资源

多任务版web服务器程序的实现步骤：
1.当客户端和服务端建立连接成功，创建子进程，使用子线程专门处理客户端的请求，防止主线程阻塞
2.把创建的子线程设置成为守护主线程，防止主线程无法退出


"""

import  socket
import  threading

# 处理客户端请求
def handle_client_request(new_socket):
    # 接受客户端的请求信息
    recv_data = new_socket.recv(4096)

    # 判断接受的数据长度是否为0
    if len(recv_data) == 0:
        new_socket.close()
        return
        # 对二进制数据进行解码
    recv_content = recv_data.decode("utf-8")
    print(recv_content)

    # 对数据按照空格进行分割
    request_list = recv_content.split("", 2)  # 也可以写成maxsplit = 2

    # 获取请求的资源路径
    request_path = request_list[1]
    print(request_path)

    # 判断请求的是否是根目录，如果是根目录设置返回的信息
    if request_path == "/":
        request_path = "/index.html"

    # 1.os.path.exists
    # os.path.exists("static/" + request_path)
    # 2.try-except

    try:
        # 打开文件读取文案金中的数据，提示：这里使用rb模式，兼容打开图片文件
        with open("static" + request_path, "rb") as file:  # 这里的file表示打开文件的对象
            file_data = file.read()
        # 提示：with open 关闭文件这步骤操作不用程序员来完成，系统帮我们来完成

    except Exception as e:
        # 代码执行到此，说明服务器没用请求该文件，返回404状态信息
        responses_line = "HTTP/1.1 404 Not Found\r\n"
        responses_header = "Server:pws/1.0\r\n"

        # 读取404页面数据
        with open("static/error.html", "rb") as file:
            file_data = file.read()
        # 响应体
        responses_body = file_data

        # 把数据封装成http 响应报文格式的数据
        responses = (responses_line +
                     responses_header +
                     "\r\n").encode("utf-8") + responses_body

        # 把字符串编码成二进制
        # responses_data = responses.encode("utf-8")

        # 发送给浏览器的响应报文数据
        new_socket.send(responses)
    else:
        # 代码执行到此，说明文件存在，返回200状态信息
        # 响应行
        responses_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        responses_header = "Server:pws/1.0\r\n"
        # 空行
        # 响应体
        responses_body = file_data
        # 把数据封装成http 响应报文格式的数据
        responses = (responses_line +
                     responses_header +
                     "\r\n").encode("utf-8") + responses_body

        # 把字符串编码成二进制
        # responses_data = responses.encode("utf-8")

        # 发送给浏览器的响应报文数据
        new_socket.send(responses)
    finally:
        # 关闭服务于客户端的套接字
        new_socket.close()

def main():
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口号复用，程序退出端口号立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(("", 8000))
    # 设置监听
    tcp_server_socket.listen(128)
    # 循环等待接受客户端的连接请求
    while True:
        # 等待接受客户端的连接请求
        new_socket, ip_port = tcp_server_socket.accept()
        # 代码执行到此，说明连接建立成功
        sub_thread = threading.Thread(target=handle_client_request, args=(new_socket,))
        # 设置成为守护主线程
        sub_thread.daemon = True

        # 启动子线程执行对应的任务
        sub_thread.start()

# 判断是否是主模块的代码
if __name__ == '__main__':
    main()

