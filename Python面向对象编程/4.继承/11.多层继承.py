"""
故事：N年后，daqiu老了，想要把所有技术传承给自己的徒弟

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

    """如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己子类的初始化"""

class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'

    def make_cake(self):
            # -- 加自己的初始化原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')
        # -- 调用父类方法，但是为保证调用到的也是父类的属性，必须在调用方法前调用父类的初始化
    def make_master_cake(self):
        Master.__init__(self)
            # -- 再次调用初始化的原因，想要调用父类的同名属性和方法，属性在init初始化位置，需要再次调用init
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# -- 徒孙类
# -- 步骤：1.创建类Tusun，用这个类创建对象；2.用这个对象调用父类的属性或方法看能否成功
class Tusun(Prentice):
    pass


xiaoqiu = Tusun()

xiaoqiu.make_cake()

xiaoqiu.make_school_cake()

xiaoqiu.make_master_cake()