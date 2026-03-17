#1.导入redis

import redis
if __name__ == '__ main__':
    #2.创建redis的连接实例
    #我们在连接/获取外界资源的时候一定要注意使用 try
    try:
        rs = redis.Redis()
    except Exception as e:
        print(e)
    
    #3.操作string
    # 添加 set ket value
    #result = rs.set('name','itcast')
    #print (result)
    
    #获取
    name = rs.get('name')
    print(name)
