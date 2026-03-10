"""

1.in: 判断指定数据在某个列表序列，如果在返回True，否则返回Flase

2.not in: 判断指定数据不在某个列表序列，如果不爱返回True，否则返回Flase



"""

# in示例：
name_list = ['Tom','Lily','Rose']
print('Lily' in name_list)
print('Lilys' in name_list)

# not in 示例：
print('Lily' not in name_list)
print('Lily' not in name_list)

# 体验案例：

# 需求：查找用户输入的名字是否已经存在
name_list = ['Tom','Lily','Rose']

name = input('请输入您要搜索的名字：')

if name in name_list:
    print(f'您输入的名字是{name}，名字已经存在')
else:
    print(f'您输入的名字是{name},名字不存在')