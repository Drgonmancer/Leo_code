"""
1.获取进程编号的目的
获取进程编号的目的是验证主进程和子进程的关系，可以得知子进程是由哪个主进程创建出来的
获取进程编号的两种操作：
    1.获取当前进程编号
    2.获取当前父进程编号

2.获取当前进程编号
os.getpid()表示获取当前进程编号

3.获取当前父进程编号
os.getppid()表示获取当前父进程编号

拓展：根据进程编号强制杀死指定进程
    os.kill(进程号，9)
代码如下：

"""
#1.导入进程包
import multiprocessing
import time
import os

# 跳舞任务
def dance():
    # 获取当前进程（子进程）的编号
    dance_process_id = os.getpid()
    print('dance_process_id:', dance_process_id, multiprocessing.current_process())
    # 获取当前进程的父进程编号
    dance_process_parent_id = os.getppid()
    print('dance_process的父进程编号是：',dance_process_parent_id)
    for i in range(3):
        print('跳舞中...')
        time.sleep(0.2)

# 唱歌任务
def sing():
    sing_process_id = os.getpid()
    print('sing_process_id:', sing_process_id, multiprocessing.current_process())
    sing_process_parent_id = os.getppid()
    print('sing_process的父进程编号是：', sing_process_parent_id)
    for i in range(3):
        print('唱歌中...')
        time.sleep(0.2)

# 获取当前进程(主进程)的编号
main_process_id = os.getpid()
# 获取当前进程对象，查看当前代码是由哪个进程执行的:multiprocessing.current_process()
print('main_process_id:',main_process_id,multiprocessing.current_process())

#2.创建子进程
dance_process = multiprocessing.Process(group='test',target=dance,name='dance_process')
print('dance_process:',dance_process)
sing_process = multiprocessing.Process(target=sing,name='sing_process')
print('sing_process:',sing_process)
print('sing_process:',sing_process)

#3.启动进程执行对应的任务
dance_process.start()
sing_process.start()