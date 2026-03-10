"""
一、创建集合
创建集合使用{}或set(),但是如果要创建空集合只能使用set(),因为{}用来创建空字典
例：
s1 = {10,20,30,40,50}
print(s1)

Ps：集合没有顺序

s2 = {10,30,20,10,30,40,30,50}
print(s2)

Ps：集合数据具有去重功能

s3 = set('abcdefg')
print(s3)

Ps：每个数据都是独立的元素呈现

s4 = set()
print(type(s4))   结果为：set

s5 = {}
print(type(s5))  结果为：dict

"""