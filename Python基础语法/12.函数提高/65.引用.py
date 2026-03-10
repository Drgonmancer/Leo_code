"""
1.了解引用：
在python中，值是靠引用来传递来的
可以用id（）来判断两个变量是否为同一个值的引用，可以将id理解为那块内存的地址标识
1)int类型
a = 1
b = a

print(b)  结果为1

发现a和b的id值相同
print(id(a))
print(id(b))

修改a的数据测试id值
a = 2
print(b)  结果为1，说明int类型为不可变类型

因为修改了a的数据，内存要开辟另外一份内存存储2，id检测a和b的地址不同
print(id(a))
print(id(b))

2) 列表
aa = [10,20]
bb = aa

print(id(aa))
print(id(bb))

aa.append(30)
print(bb)   结果为[10,20,30],列表为可变类型

a和b的id值相同
print(id(aa))
print(id(bb))

2.引用当做实参:
1)定义函数：有形参
    1.1 访问打印形参看是否有数据
    1.2 访问形参的id
    1.3 改变形参的数据，查看这个形参并打印id，看id值是否相同
2）调用函数-- 把可变和不可变两种类型依次当做实参传入

def test1(a):
    print(a)
    print(id(a))

    a += a

    print(a)
    print(id(a))

int:计算前后id值不同
b = 100
test1(b)

列表：计算前后id值相同
c = [11,22]
test1(c)

总结：
1.可变类型：
1）列表
2）字典
3）集合

2.不可变类型：
1）整型
2）浮点型
3）6.字符串
4）元组

"""