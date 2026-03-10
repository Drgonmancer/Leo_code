"""
故事推进：daqiu是个爱学习的好孩子，想学习更多的煎饼果子的技术，于是，在百度搜索到黑马程序员，报班学习煎饼果子技术

所谓多继承意思就是一个类同时继承了多个父类

Ps:当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法
代码如下：
"""

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# -- 创建学校类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class Prentice(School,Master):
    pass

# -- 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

# -- 运行结果为：[古法煎饼果子配方]
# -- 运用[古法煎饼果子配方]制作煎饼果子