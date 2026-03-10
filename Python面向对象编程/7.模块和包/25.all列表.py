"""
如果一个模块文件中有_all_变量，当使用from xxx import *导入时，只能导入这个列表中的元素
1.my_module1模块代码
_all_ = ['testA']

def testA():
    print('testA')

def testB():
    print('testB')

2.导入模块的文件代码
from my_module1 import *
testA() -- 结果打印testA
testB() -- 结果报错，因为testB函数没有添加到all列表，只有all列表里面的功能才能导入
"""