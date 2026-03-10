"""

语法：
for 临时变量 in 序列：
    重复执行的代码
    ......
else:
    循环正常结束之后要执行的代码

"""

# 示例：
str1 = 'itheima'
for i in str1:
    print(i)
else:
    print('循环正常结束之后执行的代码')

# 退出循环的方式
    # 1.break终止循环
str1 = 'itheima'
for i in str1:
    if i == 'e':
        break
    print(i)
else:
    print('循环正常结束执行的else的代码')

    # 2.continue终止循环
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)
else:
    print('循环正常结束执行的else的代码')