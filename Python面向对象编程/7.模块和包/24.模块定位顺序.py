"""
当导入一个模块，python解析器对模块位置的搜索顺序：
    1.当前目录
    2.如果不在当前目录，python则搜索在shell变量PYTHONPATH下的每个目录
    3.如果都找不到，python会查看默认路径，Unix下，默认路径一般为/usr/local/lib/python/
    模块搜素路径存储在system模块的sys.path变量中。变量里包含当前目录。PYTHONPATH和由安装过程决定的默认目录

Ps:
    1.自己的文件名不要和已有模块名重复，否则导致模块功能无法使用
    2.使用from模块名import功能的时候，如果功能名字重复，调用到的是最后定义或导入的功能

拓展：名字重复
问题：import 模块名 是否担心功能名字重复的问题 -- 不需要
import time
print(time)

time = 1
print(time)  -- 打印结果为1

问题：为什么变量也能覆盖模块？ -- 在python语言中，数据是通过引用传递的

"""