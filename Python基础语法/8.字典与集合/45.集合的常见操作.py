"""
一、增加数据
1.add(),增加的数据是单一数据
例：
s1 = {10,20}
s1.add(100)
s1.add(10)
s1.add([10,20,30])  结果为error，只能追加单一数据
print(s1)   结果为：{100，10，20}

Ps：因为集合有去重功能，所以，当向集合内部追加的数据是当前集合已有的数据的话，则不进行任何操作
集合是可变类型

2.update(),追加的数据是序列
例：
s1 = {10,20}
s1.update(100)   结果为error，update()期望的参数是一个可迭代对象（如列表、元组、集合或字符串），而不是一个单独的整数。
s1.update([100,200])
s1.update('abc')

二、删除数据
1.remove(),删除集合中的指定数据，如果数据不存在则报错
s1 = {10,20}

s1.remove(10)
print(s1)

s1.remove(10)   结果为error
print(s1)

2.discard(),删除集合中的指定数据，如果数据不存在也不会报错
s1 = {10,20}

s1.discard(10)
print(s1)

s1.discard(10)
print(s1)

3.pop(),随机删除集合中的某个数据，并返回这个数据
s1 = {10,20,30,40,50}

del_num = s1.pop()
print(del_num)
print(s1)

三、查找数据
1.in：判断数据在集合序列
2.not in：判断数据不在集合序列
3.返回值均为True或者False
例：
s1 = {10,20,30,40,50}

print(10 in s1)
print(10 not in s1)



"""