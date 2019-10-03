#!/usr/bin/env python3

# python中变量名可以是数字、字母、下划线的组合，字母区分大小写，且不能以数字开头
# = 是赋值语句，可以把任意数据类型赋值给变量
a1 = 7
print(a1)
A1 = "str"
print(A1)
a2_ = 1.23
print(a2_)

# 可以给同一变量赋不同类型的值
a1 = "str"
print(a1)

# ''和""均可表示字符串
leijun = "I'm OK"
goodgoodstudy = 'Learning python in "imooc" '
print(leijun)
print(goodgoodstudy)


# 斐波那契数列，当调用函数并输入参数x，输出数列前x位

def feibonaqi(x):
    i = 0
    a = 0
    b = 1
    while i < x:
        print(b, end=' ')
        m = b
        n = a + b
        a = m
        b = n
        i += 1


feibonaqi(5)


def feibonaqi_simple(x, i=0):
    a, b = 0, 1
    while i < x:
        print(b, end=' ')
        a, b = b, a + b
        i += 1


feibonaqi_simple(5)
