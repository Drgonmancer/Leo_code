"""
1.导入线程模块
import threading

2.线程类Thread参数说明
Thread（[group[,target[,name[,args[,kwargs]]]]])
    group:线程组，目前只能使用None
    target:执行的目标任务名
    args:以元组的方式给执行任务传参
    kwargs:以字典的方式给执行任务传参
    name:线程名，一般不用设置

3.启动线程
启动线程使用start方法

4.多线程完成多任务的代码
代码如下：
"""
# 1.导入线程模块
import threading
import time


def sing():
    # 获取当前线程
    current_thread = threading.current_thread()
    print('sing:',current_thread)
    for i in range(3):
        print('唱歌中...')
        time.sleep(0.2)

def dance():
    current_thread = threading.current_thread()
    print('dance:', current_thread)
    for i in range(3):
        print('跳舞中...')
        time.sleep(0.2)

if __name__ == '__main__':
    # 获取当前线程
    current_thread = threading.current_thread()
    print('main_thread:',current_thread)

    # 2.创建子进程
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    # 3.启动子进程执行对应的任务
    sing_thread.start()
    dance_thread.start()