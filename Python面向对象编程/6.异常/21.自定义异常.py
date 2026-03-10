"""
在python中，抛出自定义异常的语法为raise异常类对象
需求：密码长度不足，则报异常（用户输入密码，如果输入的长度不足3位，则报错，即抛出自定义异常，并捕获该异常）

代码如下：

"""

# -- 自定义异常类，继承Exception
class ShortInputError(Exception):
    def __init__(self,length,min_len):
        self.length = length
        self.min_len = min_len

    # -- 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的长度是{self.length},不能少于{self.min_len}个字符'


def main():
    try:
        con = input('请输入密码：')
        if len(con) < 3:
            raise ShortInputError(len(con),3)
    except Exception as result:
        print(result)
    else:
        print('密码已经输入完成')

main()