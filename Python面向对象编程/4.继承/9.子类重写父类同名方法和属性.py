"""
故事：daqiu掌握了师父和培训的技术后，自己潜心钻研出自己的独门配方的一套全新的煎饼果子技术

结论：如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，调用到的是子类里面的同名属性和方法

拓展：
__mro__：
用于表示方法解析顺序，它是一个元组，列出了在对象上调用方法时，Python 解释器会按照这个顺序去各个父类中查找方法。这个属性主要在涉及多继承的情况下发挥作用，帮助确定调用哪个类的方法。
代码如下：
"""

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 独创配方 -- 定义徒弟类，继承师父类和学校类，添加和父类同名的属性和方法
class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'

    def male_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# -- 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

print(Prentice.__mro__)