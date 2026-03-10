"""
1.定义私有属性和方法
在python中，可以为实例属性和方法设置私有权限，即设置某个实例或实例方法不继承给子类
故事：daqiu把技术传承给徒弟的同时，不想把自己的钱继承给徒弟，这个时候就要为钱这个实例属性设置私有权限

设置私有权限的方法：在属性名和方法名前面加上两个下划线__。

2.获取和修改私有属性值
在python中，一般定义函数名get_xx用来获取私有属性，定义set_xx用来修改私有属性值

代码如下：

"""

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'
        # -- 定义私有属性
        self.__money = 2000000
        # -- 定义私有方法

    # -- 获取私有属性
    def get_money(self):
        return self.__money

    # -- 修改私有属性
    def set_money(self):
        self.__money = 500

    def __info_print(self):
        print(self.kongfu)
        print(self.__money)

    def make_cake(self):
            # -- 加自己的初始化原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # -- 子类调用父类的同名方法和属性：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        Master.__init__(self)
            # -- 再次调用初始化的原因，想要调用父类的同名属性和方法，属性在init初始化位置，需要再次调用init
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(Prentice):
    pass


daqiu = Prentice()
# -- 对象不能访问私有属性和私有方法
# -- print(daqiu.__money)
# -- daqiu._info_print()

xiaoqiu = Tusun()
# -- 子类无法继承父类的私有属性和私有方法
# -- print(xiaoqiu.__money)  无法访问实例属性__money
# -- xiaoqiu._info_print()

# -- 调用get_money函数获取私有属性money的值
print(xiaoqiu.get_money())
# -- 调用set_money函数修改私有属性money的值
xiaoqiu.set_money()
print(xiaoqiu.get_money())
