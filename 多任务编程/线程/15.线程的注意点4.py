"""
 4.线程之间共享全局变量数据出现错误问题
 需求：
 1.定义两个函数，实现循环100万次，每循环一次给全局变量加1
 2.创建两个子线程执行对应的两个函数，查看计算后的结果

解决办法：
线程同步保证同一时刻只能有一个线程去操作全局变量
同步：就是协同步调，按预定的先后次序进行运行

线程同步的方式：
1.线程等待（join）
2.互斥锁
 代码如下：
"""

import threading

# 全局变量
g_num = 0

def task1():
    for i in range(1000000):
        # 每循环一次给全局变量加1
        # 表示要声明修改全局变量的内存地址
        global g_num
        g_num = g_num + 1

        # 代码执行到此，说明数据计算完成
        print('task1:',g_num)

def task2():
    for i in range(1000000):
        # 每循环一次给全局变量加1
        # 表示要声明修改全局变量的内存地址
        global g_num
        g_num = g_num + 1

        # 代码执行到此，说明数据计算完成
        print('task2:',g_num)

if __name__ == '__main__':
    # 创建两个子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    # 启动线程执行任务
    first_thread.start()
    # 线程等待，让第一个线程先执行，然后让第二个线程再执行，保证数据不会有问题
    first_thread.join()
    second_thread.start()
