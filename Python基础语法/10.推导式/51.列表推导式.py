"""
一、带if的列表推导式：
需求：创建0-10的偶数列表
方法一：range()步长实现：
list1 = [i for i in range(0,10,2)]
print(list1)

方法二：带if的列表推导式实现
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)

方法三：for循环加if创建有规律的列表
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)

print(list2)

二、多个for循环实现列表推导式：
需求：创建表如下：
[(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
方法一：
list1 = []
for i in range(1,3)
    for j in range(3):
        list.append(i,j)

print(list1)

方法二：
list2 = [(i,j) for i in range(1,3) for j in range(3)]
print(list2)
当 `i=1` 时，`j` 可以是 0, 1, 2，所以生成的元组是 (1,0)、(1,1)、(1,2)。
当 `i=2` 时，`j` 仍然可以是 0, 1, 2，所以生成的元组是 (2,0)、(2,1)、(2,2)。





"""