"""

一、增：
写法：字典序列[key] = 值
Ps：如果key存在则修改这个key对应的值；如果key不存在则新增此键值对
例：
dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}
dict1['name'] = 'Rose'
print(dict1)    结果为： { 'name': 'Rose', 'age': 20, 'gender': '男’}

dict1['id'] = 110
print(dict1)
结果为： {’name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}
Ps:字典为可变类型

二、删除：
1.del()/del:删除字典或删除字典中指定键值对
dict1 = { 'name': 'TOM', 'age': 20, 'gender': ‘男'}

del dict1['gender']
print(dict1)
结果为：{'name': 'TOM', 'age': 20}

2.clear():清空字典
dict1 = { 'name': 'TOM', 'age': 20, 'gender': '男'}

dict1.clear()
print(dict1)   结果是{}

三、修改：
写法：字典序列[key] = 值
Ps：如果key存在则修改这个key对应的值；如果key不存在则新增此键值对

四、查：
1.key值查找：
dict1 = { 'name': 'TOM', 'age': 20, 'gender': '男'}
print(dict1['name']   结果为TOM
print(dict1['id'])    结果为报错

Ps：如果当前查找的key存在，则返回对应的值；否则则报错

2.get():
语法：字典序列.get(key,默认值)
Ps:如果当前查找的key不存在则返回第二个参数(默认值），如果省略第二个参数，则返回None

3.keys():
dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}
print(dict1.keys())   结果为 dict_keys(['name', 'age', 'gender'])

4.values():
dict1 = { 'name': 'TOM', 'age': 20, 'gender': '男'}
print(dict1.values())    结果为dict_values([ 'TOM', 20 , '男'])

5.items():
dict1 = { 'name': 'TOM', 'age': 20, 'gender': '男'}
print(dict1.items())    结果为dict_items([('name', 'TOM'),('age',20),('gender','男')])

"""