"""
一、概念
python模块（module）,是一个python文件,以.py结尾，包含了python对象定义和python语句。
模块定义函数、类和变量，模块里也能包含可执行的代码。

1.1 导入模块
1.1.1 导入模块的方式
    1.import模块名
    2.from模块名import功能名
    3.from模块名import*
    4.import模块名as别名
    5.from模块名import功能名as别名

1.1.2 导入方式详解
1）import
语法：
# -- 1.导入模块
import 模块名
import 模块名1，模块名2...

# -- 2.调用功能
模块名.功能名（）
实例：
import math
print(math.sqrt(9)) # -- 3.0

2) from...import..
语法：
from 模块名 import 功能1，功能2，功能3...;功能调用（不需要书写模块名.功能）
实例：
from math import sqrt
print(sqrt(9))

3）from..import*; 功能调用（不需要书写模块名.功能）
语法：
from模块名import*
实例：
from math import*
print(sqrt(9))

4）as定义别名
语法：
# -- 模块定义别名
import 模块名 as 别名

# -- 功能定义别名
from 模块名 import 功能 as 别名
实例：
# -- 模块别名
import time as tt

tt.sleep(2)
print('hello')

# -- 功能别名
from time import sleep as s1
s1(2)
print('hello')
"""