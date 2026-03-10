"""
1.位置参数：调用函数时根据函数定义的参数位置来传递参数
def user_info(name,age,gender):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')

user_info('TOM',20,'男')

Ps:传递和定义参数的顺序及个数必须一致，否则前者导致数据无意义，后者会报错

2.关键字参数：函数调用，通过“键=值”形式加以指定，可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求
def user_info(name,age,gender):
    print(f'您的名字是{name},年龄是{age}，性别是{gender}')

    user_info('Rose',age=20,gender='女')
    user_info('小明',gender='男'，age=16)

Ps:函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序。

3.缺省参数：
缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值
Ps：所有位置参数必须出现在默认参数前，包括函数定义和调用
def user_info(name,age,gender = '男'):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')

user_info('TOM',20)
user_info('Rose',18,'女')

Ps:函数调用时，如果为缺省参数传值则修改默认参数值；否则使用这个默认值

4.不定长参数：
不定长参数也叫可变参数，用于不确定调用的时候会传递多少个参数（不传参也可以）的场景。此时，可以包裹位置参数，或者包裹关键字参数来进行参数传递，会显得非常方便
1）包裹位置传递：
def user_info(*args):
    print(args)

user_info('TOM')
user_info('TOM',18)

Ps:传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组，args是元组类型，这就是包裹位置传递

2）包裹关键字传递：
def user_info(**kwargs):
    print(kwargs)

user_info(name = 'TOM',age = 18,id = 110)

综上：无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程

"""