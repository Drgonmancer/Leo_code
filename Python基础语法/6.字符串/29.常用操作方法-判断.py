"""

所谓判断即是判断真假，返回的结果是布尔型数据类型：True 或 False
1.startswith(): 检查字符串是否以指定子串开头，是则返回True，否则返回Flase。如果设置开始和结束位置下标，则在指定范围内检查
语法：
字符串序列.startswith(子串，开始位置下标，结束位置下标)

2.endswith(): 判断字符串是否以某个子串结尾

3.isalpha(): 如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回Flase。

4.isdigit(): 如果字符串只包含数字则返回True，否则返回Fase

5.isalnum(): 如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回Flase

6.isspace(): 如果字符串中只包含空白，则返回True，否则返回Flase

"""

# stratswith()示例：
mystr = 'hello world and itcast and itheima and python'
print(mystr.startswith('hello'))
print(mystr.startswith('hel'))
print(mystr.startswith('hels'))

# endswith()示例：判断字符串是否以某个子串结尾
print(mystr.endswith('python'))
print(mystr.endswith('pythons'))