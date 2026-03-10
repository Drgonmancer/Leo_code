"""

作用：增加指定数据列表中。
1.append(): 列表结尾追加数据
语法：
列表序列.append(数据)
列表追加数据的时候，直接在原列表里面追加了指定数据，即修改了原列表，故列表为可变类型数据
注意点：
如果append()追加的数据是一个序列，则追加整个序列到列表

2.extend():列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
语法：
列表序列.extend(数据)

3.insert(): 指定位置新增数据
语法：
列表序列.insert(位置下标，数据)

"""

# append示例：
name_list = ['Tom','Lily','Rose']
name_list.append('xiaoming')
print(name_list)

# extend()示例：
name_list = ['Tom','Lily','Rose']
name_list.extend('xiaoming')
print(name_list)

name_list.extend(['xiaoming','xiaohong'])
print(name_list)

# insert示例：
name_list = ['Tom','Lily','Rose']
name_list.insert(1,'xiaoming')
print(name_list)





