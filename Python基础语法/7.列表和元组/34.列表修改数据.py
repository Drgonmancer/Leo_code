"""
1.修改指定下标数据

2.逆序：reverse()

3.排序：sort()
语法：
列表序列.sort( key = None, reverse = Flase)
Ps: reverse表示排序规则，reverse = True降序，reverse = False升序（默认）




"""

# 实例一：
name_list = ['Tom','Lily','Rose']
name_list[0] = 'aaa'
print(name_list)

# 示例二：
list1 = [1,5,2,3,6,8]
list1.reverse()
print(list1)  # 结果为：[8,6,3,2,5,1]

# 示例三：
list.sort(reverse=True)
print(list1)

