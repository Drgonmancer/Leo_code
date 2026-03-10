"""

输入的语法：input（“提示的信息”）
特点：
1.当程序执行到input，等待用户输入，输入完成之后才继续向下执行
2.在Python中，input接受用户输入后，一般存储到变量，方便使用
3.在Python中，input会把收到的任意用户输入的数据都当作字符串处理

"""
password =  input("请输入您的密码：")
print(f'您输入的密码是{password}')
print(type(password))