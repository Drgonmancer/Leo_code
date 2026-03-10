"""
需求：用户输入当前目录下任意文件名，程序完成对该文件的备份功能（备份文件名为xx[备份]后缀，如：test[备份].txt）
3.1 步骤：
1.接收用户输入的文件名
old_name = input('请输入您想要备份的文件名：')
print(old_name)
print(type(old_name))

2.规划备份文件名
    2.1 提取目标文件后缀 -- 找到名字中的点 -- 名字和后缀分离 -- 最右侧的点才是后缀的点 -- 字符串查找某个子串rfind
    index = old_name.rfind('.')
    print(index)   后缀中.的下标

    2.2 组织备份的文件名，xx[备份]后缀 = 原名字 + [备份] + 后缀
    Ps:原名字就是字符串中的一部分子串 -- 切片[开始:结束:步长]
    print(old_name[:index])  源文件名（无后缀）
    print(old_name[index:])
    new_name = old_name[:index] + '[备份]' + old_name[index:]
    print(new_name)  打印新文件名（带后缀）

3.备份文件写入数据（数据和原文件一样）
    3.1 打开源文件和备份文件
    old_f = open(old_name,'rb')
    new_f = open(new_name.'wb')
    3.2 将源文件数据写入备份文件
    Ps:如果不确定目标文件大小，循环读取写入，当读取出来的数据没有了终止循环
    while True:
        con = old_f.read(1024)
        if len(con) == 0:
            break
        new_f.write(con)
    3.3 关闭文件
    odl_f.close()
    new_f.close()

思考题：如果用户输入.txt，这是一个无效文件，程序如何更改才能限制只有有效的文件名才能备份？
思路：添加条件判断
old_name = input('请输入您要备份的文件名：')

index = old_name.rfind('.')

if index > 0:
    postfix = old_name[index:]

new_name = old_name[:index] + '[备份]' + postfix

old_f = open(old_name,'rb')
new_f = open(new_name,'wb')

while True:
    con = old_f.read(1024)
    if len(con) == 0:
    


"""