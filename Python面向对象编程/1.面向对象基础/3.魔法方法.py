"""
在Python中，_xx_()的函数叫做魔法方法，指的是具有特殊功能的函数
1.__init__():
__init__()方法的作用：初始化对象
实例：
class washer():
    def __init__(self):  -- 定义__init__,添加实例属性

    self.width = 500 -- 添加实例属性
    self.height = 800

    def print_info(self):
    print(f'洗衣机的宽度是{self.width},高度是{self.height}') -- 类里面调用实例属性

haier1 = washer()
haier1.print_info()

Ps:
1.__init__()方法，在创建一个对象时默认被调用，不需要手动调用
2.__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去

1.1 带参数的__init__():
思考：一个类可以创建多个对象，如何对不同的对象设置不同的初始化属性
答：传参数

实例：
class washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

创建对象，创建多个对象且属性值不同，调用实例方法
haier1 = washer(10,20)
haier1.print_info()

haier2 = washer(30,40)
haier2.print_info()

2.__str__()
当使用print输出对象的时候，默认打印对象的内存地址。如果类定义了_str_方法，那么就会打印从这个方法中return的数据
实例：
class washer():
    def __init__(self,width,height):
        slef.width = width
        self.height = height

    def __str__(self):
        return '这是海尔洗衣机的说明书‘

haier1 = washer(10,20)
print(haier1)

3.__del__()
当删除对象时，python解释器也会默认调用__del__()方法
实例：
class washer():
    def __init__(self,width,height):
        self.width = width
        self,height = height

    def __del__(self):
        print(f'{self}对象已经删除‘）

haier1 = washer(10,20)

del haier1

hasattr 语法
hasattr函数用于检查对象是否具有指定的属性。其语法如下：

hasattr(object, name)

object：要检查的对象。
name：要检查的属性名，以字符串形式给出。
该函数返回一个布尔值，如果对象具有指定的属性，则返回True，否则返回False。

setattr 语法
setattr函数用于为对象设置指定属性的值。如果属性不存在，则会添加该属性。其语法如下：

setattr(object, name, value)

object：要设置属性的对象。
name：要设置的属性名，以字符串形式给出。
value：要设置的属性值。
该函数没有返回值，直接修改对象的属性。
"""