"""
1.线程执行带有参数的任务的介绍
Thread类执行任务并给任务传参数有两种方式：
    1.args:表示以元组的方式给执行任务传参
    2.kwargs:表示以字典方式给执行任务传参

代码如下：
"""

import threading

def show_info(name,age):
    print('name: %s age: %d' % (name,age))

if __name__ == '__main__':
    # 创建子线程
    # sub_thread = threading.Thread(target=show_info,args=("李四", 20))
    # 启动线程执行对应的任务
    # sub_thread.start()

    sub_thread = threading.Thread(target=show_info,kwargs={'name':"王五","age":30})