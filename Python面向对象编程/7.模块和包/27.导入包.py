"""
2.2 导入包
2.2.1 方法一
import 包名.模块名

包名.模块名.功能（）

2.2.1.1 体验
导入mypackage包下的模块1，使用这个模块内的info_print1函数
import mypackage.my_module1
mypackage.my_module1.info_print1() -- 输出结果为1，my_module1

2.2.2 方法二
Ps：必须在_init_.py文件中添加_all_ = []，控制允许导入的模块列表
from 包名 import *
模块名.目标
2.2.2.1 体验
from my_package import *

my_module1.info_print1()
"""