"""
一、了解异常
当检测到一个错误时，解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的“异常”

二、异常的写法
2.1 语法：
try:
    可能发生错误的代码
except：
    如果出现异常执行的代码

2.2 实例
需求：尝试以r模式打开文件，如果文件不存在，则以w方式打开
代码如下：
try:
    f = open('test.txt','r')
    f = open('test.txt','w')

2.3 捕获指定异常
    2.3.1 语法：
    try:
        可能发生错误的代码
    except 异常类型:
        如果捕获到该异常类型执行的代码

2.3.2 代码如下：
try:
    print(num)
except NameError:
    print('有错误')

Ps：1.如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
2.一般try下方只放一行尝试执行的代码

2.3.3 捕获多个指定异常
当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写
try:
    print(1/0)

except (NameError,ZeroDivisionError):
    print('有错误')

2.3.4 捕获异常描述信息
try:
    print(num)
except (NameError,ZeroDivisionError) as result:
    print(result)

2.3.5 捕获所有异常
Exception是所有程序异常类的父类
try:
    print(num)
except Exception as result:
    print(result)

2.4 异常的else
else表示的是如果没有异常要执行的代码
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('我是else，是没有异常的时候执行的代码')

2.5 异常的finally
finally表示的是无论是否异常都要执行的代码,例如关闭文件
try:
    f = open('test.txt','r')
except Exception as result:
    f = open('test.txt','w')
else:
    print('没有异常，真开心')
finally:
    f.close()

"""