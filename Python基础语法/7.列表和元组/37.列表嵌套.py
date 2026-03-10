"""

所谓列表嵌套指的是一个列表里面包含其他的子列表
应用场景：要存储班级一、二、三三个班级学生姓名，且每个班级的学生姓名在一个列表


"""

name_list = [['Tom','Lily','Rose'],['张三','李四','王五'],['xiaoming','xiaohong','xiaolv']]
# 思考如何查找到数据“李四”？
print(name_list[2])
print(name_list[2][1])

