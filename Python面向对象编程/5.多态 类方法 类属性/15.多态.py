"""
1.了解多态：
多态指的是一类事物有多种形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）
11. 定义：多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果
1.2 好处：调用灵活，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变化

1.3 实现步骤：
    1.定义父类，并提供公共方法
    2.定义子类，并重写父类方法
    3.传递子类对象给调用者，可以看到不同子类执行效果不同

代码如下：
需求：警务人员和警犬一起工作，警犬分两种：追击敌人和追查毒品，携带不同的警犬，执行不同的任务
"""

class Dog(object):
    # -- 父类提供统一的方法，哪怕是空方法
    def work(self):
        print('指哪打哪...')

# -- 继承Dog类
class ArmyDog(Dog):
    # -- 子类重写父类同名方法
    def work(self):
        print('追击敌人...')


class DrugDog(Dog):
    def work(self):
        print('追查毒品...')


class Person(object):
    # -- 传入不同的对象，执行不同的代码，即不同的work函数
    def work_with_dog(self,dog):
        # -- 调用dog对象的work方法
        dog.work()


ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)