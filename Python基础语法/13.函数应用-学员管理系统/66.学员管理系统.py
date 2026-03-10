"""
目标：
1.应用：学员管理系统
2.递归
3.lambda表达式
4.高阶函数

一、应用：学员管理系统
1.1 系统简介
需求：进入系统显示系统功能界面，功能如下：
1、添加学员
2、删除学员
3、修改学员信息
4、查询学员信息
5、显示所有学员信息
6、退出系统
系统共6个功能，用户根据自己需求选取

1.2 步骤分析
1、显示功能界面
2、用户输入功能序号
3、根据用户输入的功能序号，执行不同的功能（函数）
    3.1 定义函数
    3.2 调用函数

1.3 需求实现
1.3.1 显示功能界面

1.3.2 定义不同功能的函数
所有功能函数都是操作学员信息，所有存储所有学员信息应该是一个全局变量，数据类型为列表
info = []

1.3.2.1 添加学员
需求分析：
1.接收用户输入学员信息，并保存
2.判断是否添加学员信息
    2.1 如果学员姓名已经存在，则报错提示
    2.2 如果学员姓名不存在，则准备空字典，将用户输入的数据追加到字典，再列表追加字典数据
3.对应的if条件成立的位置调用该函数

1.3.2.2 删除学员
需求分析：
按用户输入的学员姓名进行删除
1.用户输入目标学员姓名
2.检查这个学员是否存在
    2.1 如果存在，则列表删除这个数据
    2.2 如果不存在，则提示“该用户不存在”
3.对应的if条件成立的位置调用该函数

1.3.2.3 修改学员信息
需求分析：
1.用户输入目标学员姓名
2.检查这个学员是否存在
    2.1 如果存在，则修改这位学员的信息，例如手机号
    2.2 如果不存在，则报错
3.对应的if条件成立的位置调用该函数

1.3.2.4 查询学员信息
需求分析：
1.用户输入目标学员姓名
2.检查学员是否存在
    2.1 如果存在，则显示这个学员的信息
    2.2 如果不存在，则报错提示
3.对应的if条件成立的位置调用该函数

1.3.2.5 显示所有学员信息
需求分析：
打印所有学员信息

1.3.2.6 退出系统
在用户输入功能序号6的时候要退出系统,重点在于break终止循环

定义函数print_info,负责显示系统功能
def info_print():
    print('请选择功能-------------')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5.显示所有学员')
    print('退出系统')
    print('-'*20)

添加学员信息的函数：
def add_info():
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    global info  声明全局变量
    for i in info:
        if new_name == i['name']:
            print('该用户已经存在')
            return
            return的作用：退出当前函数，后面添加信息的代码不执行

    info_dict = {}

    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    列表追加字典
    info.append(info_dict)
    print(info)

删除学员：
def del_info():
    del_name = input('请输入要删除的学员的姓名：')
    global info
    for i in info:
        if del_name == i{'name'}
            info.remove(i)
            break
    else:
        print('该学员不存在')
    print(info)

修改学员信息：
def modify_info():
    modify_name = input('请输入要修改的学员的姓名：')

    global info
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的手机号：')
            break
    else:
        print('该学员不存在')

    print(info)

查询学员信息：
def search_info():
    search_name = input('请输入要查找的学员姓名：')
    global info
    for i in info:
        if search_name == i['name']:
            print('查找到的学员信息如下：----------')
            print(f“该学员的学号是{i['id']},姓名是{i['name'],手机号是{i['tel']}”)
            在Python的字符串格式化中，使用不同的引号主要是为了防止语法错误和提高代码的可读性。因为Python解释器会认为字符串在遇到第一个内部引号时就已经结束了，从而导致未关闭的字符串错误
            break
    else:
        print('该学员不存在')

显示所有学员信息：
def print_all():
    print('学号\t姓名\t手机号')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")
系统功能需要循环使用，直到用户输入6，才退出系统
while True:
info_print()

user_num = int(input('请输入功能序号'))

if user_num == 1:
    add_info()
elif user_num == 2:
    del_info()
elif user_num == 3:
    modify_info()
elif user_num == 4:
    search_info()
elif user_num == 5:
    print_all()
elif user_num == 6:
    exit_flag = input('确定要退出吗？ yes or no')
    if exit_flag == 'yes':
        break
else:
    print('输入的功能序号有误')

"""