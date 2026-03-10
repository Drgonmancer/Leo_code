"""
1.lambda的应用场景：
如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化

2.lambda语法：
lambda 参数列表 ：表达式
Ps:
1.lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用
2.lambda表达式能接受任何数量的参数但只能返回一个表达式的值。
例：
函数：
def fn1():
    return 100


print(fn1)
print(fn1())



lambda表达式：
fn2 = lambda：100
print(fn2)   结果是lambda内存地址
print(fn2())  结果为100

Ps: 直接打印lambda表达式，输出的是此lambda的内存地址。

3.示例：计算a + b
3.1 函数实现：
def add(a,b)
    return a + b


result = add(1,2)
print(result)

3.2 lambda实现：
fn1 = lambda a,b: a + b
print(fn1(1,2))

4.lambda的参数形式：
4.1 无参数：
lambda：表达式
fn1 = lambda: 100
print(fn1())
简化后：
print((lambda:100)())

4.2 一个参数：
lambda 参数：表达式
fn1 = lambda a: a
print(fn1('hello world')
简化后：
print(lambda a:a)('hello world'))

4.3 默认函数：
lambda key = value: 表达式
fn1 = lambda a,b,c=100: a + b + c
print(fn1(10,20))
简化后：
print((lambda a,b,c=100: a + b + c)(10,20))

4.4 可变参数：*args:
lambda *args：表达式
fn1 = lambda *args: args
print(fn1(10,20,30))
简化后：
print((lambda *args: args)(10,20,30))
Ps:这里的可变参数传入到lambda之后，返回值为元组

4.5 可变参数：**kwargs:
lambda **kwargs：表达式
fn1 = lambda **kwargs: kwargs
print(fn1(name = 'python',age = 20))
print((lambda **kwargs:kwargs)(name='python',age=20))
Ps:这里的可变参数传入到lambda之后，返回值为字典

5.lambda的应用：
5.1 带判断的lambda：
fn1 = lambda a,b: a if a > b else b
print(fn1(1000,500))

5.2 列表数据按字典key的值排序
students = [
    {'name': 'TOM','age':20},
    {'name': 'ROSE','age': 19},
    {'name': 'JACK','age': 22}
]
按name值升序排列
students.sort(key = lambda x: x['name'])
print(students)

按name值降序排列
students.sort(key = lambda x: x['name'],reverse = True)
print(students)
Ps:reverse参数的作用是控制排序的顺序：

按age值升序排列
students.sort(key = lambda x: x['age'])
print(students)

"""