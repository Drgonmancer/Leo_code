"""

1.del:
语法：
del 目标

2.pop(): 删除指定下标数据（默认为最后一个），并返回该数据
语法：
列表序列.pop(下标)

3.remove(): 移除列表中某个数据的第一个匹配项
语法：
列表序列.remove(数据)

4.clear() -- 清空列表

"""
from enum import nonmember

# 删除列表：
name_list = ['Tom','Lily','Rose']
del name_list
print(name_list)  # 报错

# 删除指定数据：
del name_list[0]
print(name_list)

# pop()示例：
del_name = name_list.pop(1)
print(del_name)
print(name_list)

# remove(数据)
name_list.remove('Rose')
print(name_list)

# clear() -- 清空
name_list.clear()
print(name_list)


