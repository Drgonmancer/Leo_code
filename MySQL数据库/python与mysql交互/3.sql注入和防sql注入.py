"""
6.防止SQL注入
什么是SQL注入?
用户提交带有恶意的数据与SQL语句进行字符串方式的拼接，从而影响了SQL语句的语义，最终产生数据泄露的现象。

如何防止SQL注入?
SQL语句参数化
1.SQL语言中的参数使用%s来占位，此处不是python中的字符串格式化操作
2.将SQL语句中%s占位所需要的参数存在一个列表中，把参数列表传递给execute方法中第二个参数
防止SQL注入的示例代码:
"""
from socket import fromfd

import pymysql
from pymysql import connect, Connect, Connection
from select import select

if __name__ == '__main__':
    # 2.创建连接对象
    # conn =  Connection = Connect
    # 本质上是一个函数，使用这三个里面的任何一个函数都可以创建一个连接对象
    # 1.host:服务器的主机地址
    # 2.port:mysql数据库的端口号
    # 3.user:用户名
    # 4.password:密码
    # 5.database:操作的数据库
    # 6.charset:操作数据库使用的编码格式
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="mysql",
                           database="python41",
                           charset="utf-8")

    # 3.获取游标，目的就是要执行sql语句
    cursor = conn.cursor()
    # 准备sql，使用防止sql注入的sql语句
    sql = "select * from students where name = %s;"
    print(sql)
  # sql = "select * from students where name = '%s';" % "黄蓉' or 1 = 1 or'"
    # 4.执行sql语句
    cursor.execute(sql,("黄蓉' or 1 = 1 or'",))
    # 5.关闭游标
    cursor.close()
    # 6.关闭连接
    conn.close()