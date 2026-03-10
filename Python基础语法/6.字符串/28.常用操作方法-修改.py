"""

所谓修改字符串，指的是通过函数的形式修改字符串中的数据
1.replace():替换
语法：
字符串序列.replace(旧子串，新子串，替换次数）
Ps: 数据按照是否能直接修改分为可变类型和不可变类型两种，字符串类型的数据修改的时候不能改变原有字符串，属于不能直接修改数据的类型即是不可变类型

2.split(): 按照指定字符分割字符串-- 分割，返回一个列表，丢失分割字符
1.语法
字符串序列.split(分割字符，num)
Ps: num表示的是分割字符出现的次数，即将来返回数据个数为num+1个

3.join(): 用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串
语法：
字符或子串.join(多字符串组成的序列)

4. capitalize(): 将字符串第一个字符转换成大写
Ps: capitalize()函数转换后，只字符串第一个字符大写，其他的字符全都小写

5.title(): 将字符串每个单词首字母转换成大写

6.lower(): 将字符串中大写转小写

7.upper(): 将字符串中小写转大写

8.lstrip(): 删除字符左侧空白字符

9.rstrip(): 删除字符串右侧空白字符

10.strip(): 删除字符串两侧空白字符

11.ljust(): 返回一个原字符串左对齐，并使用指定字符（默认空格）填充至对应长度的新字符串
语法：
字符串序列.ljust(长度，填充字符)

12.rjust(): 返回一个原字符串右对齐，并指定字符（默认空格）填充至对应长度的新字符串，语法和ljust()相同

13.center(): 返回一个原字符串居中对齐，并指定字符（默认空格）填充至对应长度的新字符串，语法和ljust()相同


"""

# 1.replace()示例：
mystr = 'hello world and itcast and itheima and python'
# replace() 把and换成he  说明replace函数有返回值，返回值是修改后的字符串
new_str = mystr.replace('and','he')
new_str = mystr.replace('and','he',1)
# 替换次数如果超出了串出现的次数，表示替换所有这个子串
print(mystr)
print(new_str)
# 调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
# 说明字符串是不可变数据类型

# 2.split()示例：
list1 = mystr.split('and')  # 结果是去掉所有的and，每个字符之间用，隔开
list1 = mystr.split('and',2)  # 结果为去掉两个and
print(list1)

# 3.join()示例：
list1 = ['chuan','zhi','bo','ke']
print('_'.join(list1))  # 结果为：chuan_zhi_bo_ke

