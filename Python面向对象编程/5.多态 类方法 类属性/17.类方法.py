"""
1.类方法
1.1 类方法特点：
    需要用装饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一参数

1.2 类方法使用场景
    1.当方法中需要使用类对象（如访问私有类属性等）时，定义类方法
    2.类方法一般和类属性配合使用

代码如下：

"""

class Dog(object):
    __tooth = 10

    # -- 定义类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth


wangcai = Dog()
result = wangcai.get_tooth()
print(result)  # -- 结果为10