"""
一、遍历字典的key
例：
dict1 = {'name': 'TOM', 'age':20, 'gender':'男'}
for key in dict1.key():
    print(key)

结果为：name age gender

二、遍历字典的value
dict1 = {'name': 'TOM', 'age':20, 'gender': '男'}
for value in dict1.values():
    print(value)

结果为：TOM 20 男

三、遍历字典的元素
dict1 = {'name':'TOM', 'age':20, 'gender': '男'}
for item in dict1.items():
    print(item)

结果为：（'name', 'TOM'） （'age',20） （'gender','男'）

四、遍历字典的键值对
dict1 = {'name':'TOM', 'age':20, 'gender': '男'}
for key, value in dict1.items():
    print(f'{key} = {value}')

结果为：name = TOM  age = 20  gender = 男
Ps：xx.items()：返回可迭代对象，内部是元组，元组有2个数据
元组数据1是字典的key，元组的数据2是字典的value

"""