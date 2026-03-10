"""
需求：
1.尝试只读方式打开test.txt文件，如果文件存在则读取文件内容，文件不存在则提示使用户即可
2.读取内容要求：尝试循环读取内容，读取过程中如果检测到用户意外终止程序，则except捕获异常并提示用户

代码如下：

拓展：命令提示符

"""

import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
    # -- 如果在读取文件的过程中，产生了异常，那么就会捕获到
    # -- 比如按下ctrl + c,在命令提示符中按下可以结束终止的键
        print('意外终止了读取数据')
except:
    print('该文件不存在')
