"""
1.局部变量：
所谓局部变量定义在函数体内部的变量，即只在函数体内部生效
def testA():
    a = 100

    print(a)

testA()    结果为100
print(a)   报错

原因：变量a是定义在testA函数内部的变量，在函数外部访问则立即报错

局部变量的作用：在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量

2.全局变量：
所谓全局变量，指的是在函数体内、外部能生效的变量
定义全局变量a
a = 100

def testA():
    print(a)   结果为访问全局变量a，并打印变量a存储的数据

def testB():
    print(a)   访问全局变量a，并打印变量a存储的数据

testA()
testB()

3.修改全局变量：
Q1：testB函数需求修改变量a的值为200，如何修改？
def testA():
    print(a)

def testB():
    a = 200
    print(a)

testA()  结果为100
testB()  结果为200
print(f'全局变量a = {a}')   全局变量a = 100

"""