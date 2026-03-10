"""
3.1 student.py
需求：
    学员信息包含：姓名、性别、手机号
    添加_str_魔法方法，方便查看学员对象信息
3.1.2 程序代码
"""

class Student(object):
    def __init__(self,name,gender,tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'

