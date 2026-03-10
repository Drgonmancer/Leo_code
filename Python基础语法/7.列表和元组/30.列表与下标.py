"""

列表格式：
[数据1，数据2，......]
列表可以一次性存储多个数据，且可以为不同的数据类型
列表的常用操作：
列表的作用是一次性存储多个数据，常用操作：增、删、改、查
1.查找:
下标
函数：
1）index(): 返回指定数据所在位置的下标
语法：
列表序列.index(数据，开始位置下标，结束位置下标)
Ps: 如果查找的数据不存在则报错

2）count(): 统计指定数据在当前列表中出现的次数

3）len(): 访问列表长度，即列表中数据的个数
语法：
len(列表序列) 

"""

# 下标示例：
name_list = ['Tom','Lily','Rose']

print(name_list[0])   # Tom
print(name_list[1])
print(name_list[2])

# index()示例：
print(name_list.index('Tom'))
print(name_list.index('Toms'))

# count()示例：
print(name_list.count('Tom'))
print(name_list.count('Toms'))

# len()示例：
print(len(name_list))
