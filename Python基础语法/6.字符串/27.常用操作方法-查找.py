"""

字符串的常用操作方法有查找、修改和判断三大类
1.查找：
所谓字符串查找方法即是查找在字符串中的位置或出现次数
1) find（）：检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则返回-1
语法：
字符串序列：find（子串，开始位置下标，结束位置下标）
Ps：开始和结束位置下标可以省略，表示在整个字符串序列中查找
2) index(): 检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则
报异常。
语法：
字符串序列． index （子串，开始位置下标，结束位置下标）
Ps：开始和结束位置下标可以省略，表示在整个字持串序列中查找。

其他方法：
rfind(): 和find()功能相同，但查找方向为右侧开始
rindex(): 和index()功能相同，但查找方向为右侧开始
count(): 返回某个子串在字符串中出现的次数
语法：
字符串序列.count(子串，开始位置下标，结束位置下标)
Ps:开始和结束位置下标可以省略，表示在整个字符串序列中查找

"""

# find（）示例：
mystr = 'hello world and itcast and itheima and pyhton'

print(mystr.find('and'))  # 12
print(mystr.find('and',15,30))  # 23
print(mystr.find('ands'))  # -1

# index（）示例：
print(mystr.index('and'))  # 12
print(mystr.index('and',15,30))  # 23
print(mystr.index('ands'))  # 报错

# count（）示例：
print(mystr.count('and',15,30)) # 1
print(mystr.count('and'))  # 3
print(mystr.count('ands')) # 0

# rfind（）示例：
print(mystr.rfind('and'))  # 35
print(mystr.rfind('ands')) # -1

# rindex（）示例：
print(mystr.rindex('and')) # 35
print(mystr.rindex('ands')) # 报错
