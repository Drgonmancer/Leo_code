"""
公共方法：
len():计算容器元素个数
del或del():删除
max():返回容器中元素最大值
min():返回容器中元素最小值
range(start,end,step):生成从start到end的数字，步长为step，供for循环使用
enumerate():函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中

1.len():
str1 = 'abcdefg'
print(len(str1))   结果为7

list1 = [10,20,30,40,50]
t1 = (10,20,30,40,50)
s1 = {10,20,30,40,50}
结果均为5

dict1 = {'name': 'TOM', 'age': 18}
print(len(dict1))   结果为2，统计键值对的个数

2.del或del():
str1 = 'abcdefg'
list1 = [10,20,30,40,50]
t1 = (10,20,30,40,50)
s1 = {10,20,30,40,50}
dict1 = {'name': 'TOM', 'age': 18}

del str1
print(str1)    检验是否删除字符串

del(list1)
print(list1)    检验是否删除列表
del(list[0])   删除下标为0的数据
print(list1)

del s1
print(s1)

del dict1
print(dict1)
del dict1['name']   删除某一个键值对
print(dict1)

3.max()和min():
str1 = 'abcdefg'
list1 = [10,20,30,40,50]

max():最大值
print(max(str1))
print(min(list1))
结果为g 10

min():最小值
print(min(str1))
print(min(list1))
结果为a 10

4.range(start,end,step):
输出1-9：
for i in range(1,10,1):
    print(i)

输出1，3，5，7，9：
for i in range(1,10,2):
    print(i)

输出0-9：
for i in range(10):
    print(i)
Ps:1.range()生成的序列不包含end数字
2.如果不写开始，默认从0开始
3.如果不写步长，默认为1

5.enumerate():
enumerate返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据
语法：enumerate(可遍历对象，start = 0)
Ps:start参数用来设置遍历数据的下标的起始值，默认为0
例：
list1 = ['a','b','c','d','e']

for i in enumerate(list1):
    print(i)

结果为（下标，'数据'）

for index,char in enumerate(list1,start = 1):
    print(f'下标是{index}，对应的字符是{char}‘）






"""