"""
self:指的是调用该函数的对象
1.定义类
 class washer():
    def wash(self):
        print('我会洗衣服')
        print(self)

2.创建对象
haier1 = washer()
print(haier1)
haier1.wash() -- haier1对象调用实例方法

haier2 = washer()
haier2.wash()

Ps:1.一个类可以创建多个对象
2.多个对象都调用函数的时候，self地址是否相同(不同)

三、添加和获取对象属性
属性即是特征，对象属性既可以在类外面添加和获取，也能在类里面添加和获取
3.1 类外面添加对象属性
语法：
对象名.属性名 = 值
例：
haier1.width = 500

3.2 类外面获取对象属性
语法：
对象名.属性名
例：
print(f'haier1洗衣机的宽度是{haier1.width}')

3.3 类里面获取对象属性
语法：
self.属性名
class washer():
    def print_info(self):
        print(f'洗衣机的宽度是{self。width}')

haier1.print_info()

"""