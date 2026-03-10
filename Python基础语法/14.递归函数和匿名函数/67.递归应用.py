"""
1.递归的作用：递归是一种编程思想：
1）如要遍历一个文件夹下面所有的文件，通常会使用递归来实现
2）算法离不开递归

2.递归的特点：
1）函数内部自己调用自己
2）必须有出口

3.应用：3以内数字累加和
def sum_numbers(num):
    if num == 1:
        return 1
    return num + sum_numbers(num-1)

sum_result = sum+numbers(3)
print(sum_result)  结果为6

"""