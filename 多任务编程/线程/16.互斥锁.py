"""
1.互斥锁的概念
互斥锁：对共享数据进行锁定，保证同一时刻只能有一个线程去操作
Ps：
互斥锁是多个线程一起去抢，抢到锁的线程先执行，没有抢到锁的线程需要等待
等互斥锁使用完释放后，其他等待的线程再去抢这个锁。

2. 互斥锁的使用
threading模块中定义了Lock变量，这个变量本质上是一个函数，通过调用这个函数可以获取一把互斥锁。
使用步骤：
创建锁
mutex = threading.Lock()

# 上锁
mutex.acquire()

...这里编写代码能保证同一时刻只能有一个线程去操作，对共享数据进行锁定...

# 释放锁
mutex.release()

Ps:
1.acquire和release方法之间的代码同一时刻只能有一个线程去操作
2.如果在调用acquire方法的时候其他线程已经使用了这个互斥锁，那么此刻acquire方法会堵塞，
直到这个互斥锁释放后才能再次上锁

互斥锁可以保证同一时刻只有一个线程去执行代码，能够保证全局变量的数据没有问题
线程等待和互斥锁都是把多任务改成单任务去执行，保证了数据的准确性，但是执行性能会下降

代码如下：
"""

import threading

# 全局变量
g_num = 0


# 创建互斥锁，Lock本质上是一个函数，通过调用函数可以创建一个互斥锁
lock = threading.Lock()

def task1():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        # 每循环一次给全局变量加1
        # 表示要声明修改全局变量的内存地址
        global g_num
        g_num = g_num + 1

        # 代码执行到此，说明数据计算完成
        print('task1:',g_num)
        # 释放锁
        lock.release()

def task2():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        # 每循环一次给全局变量加1
        # 表示要声明修改全局变量的内存地址
        global g_num
        g_num = g_num + 1

        # 代码执行到此，说明数据计算完成
        print('task2:',g_num)
        # 释放锁
        lock.release()

if __name__ == '__main__':
    # 创建两个子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    # 启动线程执行任务
    first_thread.start()
    # 线程等待，让第一个线程先执行，然后让第二个线程再执行，保证数据不会有问题
    first_thread.join()
    second_thread.start()
