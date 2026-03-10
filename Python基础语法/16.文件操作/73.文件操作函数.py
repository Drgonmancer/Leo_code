"""
在python中文件和文件夹的操作要借助os模块里面的相关功能
1.导入os模块
import os
2.使用os模块功能
os.函数名()

四、文件和文件夹操作
4.1 文件重命名
rename():重命名
语法：
os.rename(目标文件名，新文件名)
os.rename('1.txt','10.txt')

4.2 删除文件
remove():删除文件
语法：
os.remove(目标文件名)
os.remove('10.txt')

4.3 创建文件夹
mkdir():创建文件夹
语法：
os.mkdir(文件夹名字)

4.4 删除文件夹
rmdir():删除文件夹
语法：
os.rmdir(文件夹名字)

4.5 获取当前目录
语法：
os.getcwd()

4.6 改变默认目录
语法：
os.chdir(目录)

4.7 获取目录列表
语法：
os.listdir(目录)

4.8 重命名文件夹
os.rename()






"""