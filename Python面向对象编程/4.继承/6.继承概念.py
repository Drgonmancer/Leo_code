"""
拓展1：经典类或旧时类
不由任意内置类型派生出的类，称之为经典类
例：
class 类名：
    代码
    .....

拓展2：新式类
例：
class 类名(object)：
    代码

python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法
在python中，所有类默认继承object类，object类是顶级类或基类；其他子类叫做派生类
实例如下：

"""

# 父类A
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

# 子类B
class B(A):
    pass

result = B()
result.info_print() # -- 1