"""
1.线程的注意点介绍
    1.线程之间执行是无序的
    2.主线程会等待所有的子线程执行结束再结束
    3.线程之间共享全局变量
    4.线程之间共享全局变量数据出现错误问题

代码如下：
"""
import threading
import time

def task():
    time.sleep(1)
    # 获取当前线程
    print(threading.current_thread())

if __name__ == '__main__':
    # 循环创建大量线程，测试线程之间执行是否无序
    for i in range(20):
        sub_thread = threading.Thread(target=task)
    # 启动子进程执行相应的任务
        sub_thread.start()

    # 线程之间执行是无序的，具体哪个线程执行是由CPU调度决定的
    # 进程之间执行也是无序的，具体哪个进程执行是由操作系统调度进程来决定的