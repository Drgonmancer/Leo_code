"""
一般在实际开发过程中，一个程序往往由多个函数组成，并且多个函数共享某些数据
1.共用全局变量：
1）定义全局变量
glo_num = 0

def test1():
    global glo_num    声明全局变量
    修改全局变量
    glo_num = 100

def test2():
    调用test1函数中修改后的全局变量
    print(glo_num)

2）调用test1函数，执行函数内代码：声明和修改全局变量
test1()
3) 调用test2函数，执行函数内部代码：打印
test2()   结果为100

结果统计：
1.print(glo_num)  结果为0，因为修改的函数没执行
2.test2()  结果为0，因为修改的函数没执行
3.test1()
  test2()  结果为100，先调用了了函数1

2.返回值作为参数传递
def test1():
    return 50

def test2(num):
    print(num)

1) 保存函数test1的返回值
result = test1()

2) 将函数返回值所在变量作为参数传递到test2函数
test2(result)    结果为50

"""