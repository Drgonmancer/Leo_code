"""
一、运算符
+：合并，支持的容器类型：6.字符串、列表、元组
*：复制，支持的容器类型：6.字符串、列表、元组
in：元素是否存在，支持的容器类型：6.字符串、列表、元组、字典
not in：元素是否存在，支持的容器类型：6.字符串、列表、元组、字典

1.+：
Ps:字典不支持合并运算
str1 = 'aa'
str2 = 'bb'

list1 = [1,2]
list2 = [10,20]

t1 = (1,2)
t2 = (10,20)

dict1 = {'name: Python'}
dict2 = {'age: 30'}

print(str1 + str2)
print(list1 + list2)
print(t1 + t2)

2.*：
str1 = 'a'
list1 = ['hello']
t1 = ('world'，)
Ps:元组是通过将多个值用逗号分隔来创建的，即使这个元组只包含一个元素，也需要在元素后面加上逗号以区分它与普通的括号表达式。

print(str1 * 5)
print('-' * 10)
print(list1 * 5)
print(t1 * 5)

3.in 和 not in:
str1 = 'abcd'
list1 = [10,20,30,40]
t1 = (100,200,300,400)
dict1 = {'name': 'python', 'age': 30}
print('a' in str1)
print('a' not in str1)

print(10 in list1)
print(1o not in list1)

print(100 in t1)
print(100 noy in t1)

print('name' in dict1)
print('name' not in dict1)
print('name' in dict1.keys())
print('name' in dict1.values())

"""