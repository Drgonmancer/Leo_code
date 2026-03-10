"""
1.进程的注意点介绍：
    1.进程之间不共享全局变量
    2.主进程会等待所有的子进程执行结束再结束

2.进程之间不共享全局变量
创建子进程其实就是对主进程资源进行拷贝
子进程其实就是主进程的一个副本
代码如下：
"""

import multiprocessing
import time
from msilib import add_data

# 定义全局变量列表
g_list = list()

# 添加数据的任务
def add_data():
    for i in range(3):
        # 因为列表是可变类型，可以在原有内存的基础上修改数据，并且修改后内存地址不变
        # 所以不需要加上global关键字
        # 加上global 表示声明要修改全局变量的内存地址
        g_list.append(i)
        print('add:',i)
        time.sleep(0.2)
    print('添加完成：',g_list)

# 读取数据的任务
def read_data():
    print('read:',g_list)

# 提示：对应的Linux和mac主进程执行的代码不会进程拷贝，但是对应Windows系统来说主进程执行的代码也会进行拷贝
# 对于Windows来说创建子进程的代码如果进行拷贝执行相当于递归无限制进行创建子进程，会报错

# 如果解决Windows递归创建子进程，通过判断是否是主模块来解决
# 理解说明：直接执行的模块就是主模块，那么直接执行的模块里面就应该添加判断是否是主模块的代码

# 1.防止别人导入文件的时候执行main里面的代码
# 2.防止Windows系统递归和创建子进程
if __name__ == '__main__':
    # 添加数据的子进程
    add_process = multiprocessing.Process(target=add_data)
    # 读取数据的子进程
    read_process = multiprocessing.Process(target=read_data)

    # 启动数据执行对应的任务
    add_process.start()
    # 当前进程（主进程）等待添加数据的进程执行完成以后代码再继续往下执行
    add_process.join()
    read_process.start()


