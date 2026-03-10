"""
Q1: 如果一个函数有两个return，程序如何执行？
Ps:一个函数如果有多个return不能都执行，只执行第一个return，无法返回多个返回值
答：一个函数多个返回值的写法
def return_num():
    return 1,2
    return(10,20)
    return[100,200]
    return {'name':'python','age':30}

result = return_num()
print(result)

Ps:1.return a，b写法，返回多个数据的时候，默认是元组类型
2.return后面可以连接列表、元组或字典，以返回多个值

"""