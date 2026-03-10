"""
1.拆包：
1）拆包：元组
def return_num():
    return 100,200

num1,num2 = return_num()
print(num1)  结果为100
print(num2)  结果为200

2）拆包：字典
dict1 = {'name': 'TOM', 'age': 18}
a,b = dict1

对字典进行拆包，取出来的是字典的key
print(a)  结果为name
print(b)  结果为age

print(dict1[a])  结果为TOM
print(dict[b])   结果为18

2.交换变量值
需求：有变量a = 10和b = 20,交换两个变量的值
方法一：借助第三变量存储数据
1）定义中间变量：
c = 0

2）将a的数据存储到c
c = a

3)将b的数据20赋值到a，此时a = 20
a = b

4）将之前c的数据10赋值到b，此时b = 10
b = c

print(a)   结果为20
print(b)   结果为10

方法二：
a,b = 1,2
a,b = b,a
print(a)
print(b)

"""