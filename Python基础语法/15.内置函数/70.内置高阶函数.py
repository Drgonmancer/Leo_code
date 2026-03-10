"""
1.map():
map(func,lst),将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表（python2）/迭代器（python3）返回

需求：计算list1序列中各个数字的2次方
list1 = [1,2,3,4,5]

def func(x):
    return x ** 2

result = map(func,list1)

print(result)
print(list(result))   结果为[1,4,9,16,25]

2.reduce():
reduce(func,lst),其中func必须有两个参数，每次func计算的结果继续和序列的下一个元素做累积计算
Ps:reduce()传入的参数func必须接收2个参数

需求：计算list1序列中各个数字的累加和
import functools

list1 = [1,2,3,4,5]

def func(a,b):
    return a + b

result = functools.reduce(func,list1)

print(result)   结果为15

3.filter():
filter(func,lst)函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象，如果要转换成列表，可以使用list()来转换
list1 = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x % 2 == 0

result = filter(func,list1)

print(result)
print(list(result))   结果为[2,4,6,8,10]

4.count()函数
语法：
str.count(sub,start = 0,end = len(string))
参数解释：
sub - 要搜索的子字符串
start - 开始搜索字符串的位置，默认为第一个字符，第一个字符索引值为0
end - 结束搜索字符串的位置，字符中第一个字符的索引为0，默认为字符串的最后一个位置

count()函数用于统计字符串中某个字符或字符串出现的次数，且count()函数不区分大小写，只要出现就算一次

"""