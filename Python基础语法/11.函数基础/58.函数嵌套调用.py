"""
一、函数嵌套调用：
所谓函数嵌套调用指的是一个函数里面又调用了另外一个函数
例：
def testB():
    print('--- testB start---')
    print('这里是testB函数执行的代码...(省略）...')
    print('--- testB end ---')

def testA():
    print('--- testA start ---')
    testB()
    print('--- testA end ---')

testA()

实操案例：
案例一：打印图形
1.打印一条横线：
def print_line():
    print('-' * 20)

print_line()

2.打印多条横线：
def print_line():
    print('-' * 20)

def print_line(num):
    i = 0
    while i < num:
        print_line()
        i += 1

print_line(5)

案例二：
1.求三个数之和
def sum_num(a,b,c):
    return a + b + c

result = sum_num(1,2,3)
print(result)    结果为6

2.求三个数平均值
def average_num(a,b,c):
    sumResult = sum_num(a,b,c)
    return sumResult / 3

result = average_num(1,2,3)
print(result)   结果为2.0

"""