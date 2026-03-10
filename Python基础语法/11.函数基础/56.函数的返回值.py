"""
一、函数返回值的作用
在函数中，如果需要返回结果给用户需要使用函数返回值。
例：去超市购物，比如买烟，给钱之后，是不是售货员会返回给我们烟这个商品
def buy():
    return '烟‘

使用变量保存函数返回值
goods = buy()
print(goods)

return的作用：
1.负责函数返回值
2.退出当前函数，导致return下方的所有代码（函数体内部）不执行
1.应用：
需求：制作一个计算器，计算任意两个数字之和，并保存结果
def sum_num(a,b):
    return a + b

用result变量保存函数返回值
result = sum_num(1,2)
print(result)

"""