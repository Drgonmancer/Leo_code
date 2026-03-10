"""
1.进程执行带有参数的任务的介绍
前面使用进程执行的任务是没有参数的，如果使用进程执行的任务带有参数，如何给函数传参
Process类执行任务并给任务传参有两种方式：
    1.args：表示以元组的方式给执行的任务传参
    2.kwargs：表示以字典方式给执行任务传参

代码如下：
"""

import multiprocessing

#显示信息的任务
def show_info(name,age):
    print(name,age)
#创建子进程
# 以元组方式传参，元组里面的元素顺序要和函数的参数顺序保持一致
#sub_process = multiprocessing.Process(target=show_info,args=("李四", 20))
# 以字典方式传参，字典里面的key要和函数里面的参数名保持一致，没有顺序要求
# sub_process = multiprocessing.Process(target=show_info,kwargs=("age": 20, "name": '王五'))
sub_process = multiprocessing.Process(target=show_info,args=('冯七'), kwargs={"age":20})


#启动进程
sub_process.start()
