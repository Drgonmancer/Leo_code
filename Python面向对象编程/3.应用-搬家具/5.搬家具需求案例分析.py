"""
1.需求：
将小于房子剩余面积的家具摆放到房子中

2.步骤分析：
需求涉及两个事物：房子和家具，故涉及两个类：房子类和家具类

2.1 定义类
房子类
    实例属性
        房子地理位置
        房子占地面积
        房子剩余面积
        房子内家具列表
    实例方法
        容纳家具
    显示房屋信息

家具类
    家具名称
    家具占地面积

2.2 创建对象并调用相关方法


代码如下：
"""

class Furniture():
    def __init__(self,name,area):
        self.name = name # -- 家具名字
        self.area = area # -- 家具占地面积

class Home():
    def __init__(self,address,area):
        self.address = address # -- 地理位置
        self.area = area # -- 房屋面积
        self.free_area = area # -- 剩余面积
        self.furniture = [] # -- 家具列表

    def __str__(self):
        return f'房子地理位置在{self.address},房屋面积是{self.area},剩余面积{self.free_area},家具有{self.furniture}'

    def add_furniture(self,item):  # -- 容纳家具
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area # -- 家具搬入后，房屋剩余面积 = 之前剩余面积 - 该家具面积

        else:
            print('家具太大，剩余面积不足，无法容纳')

bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 10)

jia1 = Home('北京',1000)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

ball = Furniture('篮球场',2000)
jia1.add_furniture(ball)
print(jia1)