import sys
from sqlite3.dbapi2 import paramstyle

# 获取终端命令行参数
params = sys.argv

# 列表里面的每项数据都是字符串类型
print(params,type(params))