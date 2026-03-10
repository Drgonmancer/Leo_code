"""
验证索引性能操作:
-- 开启运行时间监测:
set profiling=l;

-- 查找第1万条数据ha-99999
select * from test_index where title='ha-99999';

-- 查看执行的时间:
show profiles;

-- 给title字段创建索引:
alter table test_index add index (title);

-- 再次执行查询语句
select * from test_index where title='ha-99999';

-- 再次查看执行的时间
show profiles;
"""
import pymysql

if __name__ == '__main__':
    # 创建连接对象
    conn = pymysql.connect(host="localhost",
                    port=3306,
                    user="root",
                    password="mysql",
                    database="python41",
                    charset="utf-8")
    # 获取游标，目的是执行sql语句
    cursor = conn.cursor()
    # 准备sql
    sql = "insert into mytest(name) value(%s);"

    try:
        # 循环执行10000次插入数据的操作
        for i in range(10000):
            # 执行sql
            cursor.execute(sql,["test" + str(i)])

        # 代码执行到此说明添加数据完成，那么提交数据到数据库
        conn.commit()
    except Exception as e:
        # 回滚数据，回到插入之前的一个状态
        conn.rollback()

    finally:
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()