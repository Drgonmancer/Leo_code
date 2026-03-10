"""
一、列表推导式应用：
例：需求：创建一个0-10的列表
1.while循环实现：
list1 = []

i = 0
while i < 10:
    list1.append(i)
    i += 1

print(list1)

2.for循环实现：
list1 = []
for i in range(10):
    list1.append(i)

print(list1)

3.列表推导式实现：
list1 = [i for i in range(10)]
print(list1)

"""