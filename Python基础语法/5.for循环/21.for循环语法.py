"""

语法：
for 临时变量 in 序列：
    重复执行的代码1
    .......

"""
# 举例代码一(break 打破 5.for循环)：
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)

# 举例代码二(continue 打破 5.for循环)：、
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)