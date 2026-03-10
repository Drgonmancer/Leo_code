"""
字典推导式：
作用：快速合并列表为字典或提取字典中目标数据
例：
1.创建一个字典：字典key是1-5数字，value是这个数字的2次方
dict1 = {i: i**2 for i in range(1,5)}
print(dict1)

2.将两个列表合并为一个字典
list1 = ['name', 'age', 'gender']
list2 = ['TOM', 20, 'man']

dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)

Ps:zip函数：
语法：
zip(*iterables)
*iterables:表示一个或多个可迭代对象

dict1 = dict(zip(list1,list2))
print(dict1)

3.提取字典中目标数据：
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo':199, 'acer': 99}

需求：提取上述电脑数量大于等于200的字典数据
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)    结果为{'MBP':268, 'DELL':201}

"""