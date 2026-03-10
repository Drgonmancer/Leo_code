"""
super()函数:
主要用于调用父类（即超类）的方法。它通常在子类的方法中使用，以便访问或调用父类的方法，尤其是在子类重写了父类的方法时，保证父类的方法也能被正确调用。

Ps:使用super()可以查找父类，调用顺序遵循__mro__类属性的顺序，比较适合单继承使用

"""

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    # --方法一：super()带参数写法
    # -- super(School,self).__init__()
    # -- super(School,self).make_cake()

    # -- 方法二：无参数的super()
    super().__init__()
    super().make_cake()


class Prentice(School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'

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

    # -- 一次性调用父类的同名属性和方法
    def make_old_cake(self):
        # -- 方法一：代码冗余：父类类名如果变化，这里代码需要频繁修改
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        # -- 方法二：super()
        # 方法2.1 super(当前类名，self).函数()
        # super(Prentice,self).__init__()
        # super(Prentice,self).make_cake()

        # -- 方法2.2 super().函数()
        super().__init__()
        super().make_cake()

daqiu = Prentice()

daqiu.make_old_cake()