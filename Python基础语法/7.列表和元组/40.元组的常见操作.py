"""

一、元组的常见操作-查找
1.元组数据不支持修改，只支持查找，具体如下：
1）按下标查找数据：
tuple1 = ('aa','bb','cc','dd')
print(tuple[0]    结果为aa

2）index（）：查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index方法相同
tuple1 = ('aa','bb','cc','dd')
print(tuple1.index('aa'))  结果为0

3）count（）：统计某个数据在当前元组出现的次数
tuple1 = ('aa','bb','cc','dd')
print(tuple1.count('bb'))   结果为2

4）len（）：统计元组中数据的个数
tuple1 = ('aa','bb','cc','dd')
print(len(tuple1))   结果为4

二、元组的常见操作-修改
Ps：元组内的直接数据如果修改则立即报错
tuple1 = ('aa','bb','cc','dd')
tuple1[0] = 'aaa'

但是如果元组里面有列表，修改列表里面的数据则是支持的，故自觉很重要
tuple2 = (10,20,['aa','bb','cc'],50,30)
print(tuple2[2])   访问到列表

tuple2[2][0] = 'aaaaa',
print(tuple2)
结果为（10，20，['aaaaa','bb','cc'],50,30)
"""