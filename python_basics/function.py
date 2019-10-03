#!/usr/bin/env python3
from typing import Any, Callable


def helloworld():
    print('Hello World!')


def area(width, height):
    return width * height


def welcome(name):
    print('Welcome,', name)


# 函数可以定义默认参数，当调用方法时如果未传值则使用默认参数
def animal(name, an='dog'):
    print('小动物名字是：' + name, '它是一只' + an)


# 可变长参数
# 用*表示多个，参数会以tuple的形式传入
# 用**表示多个，参数会以dict的形式传入，dict是key-value形式，此时调用的时候可变参数位置要用关键字参数
# 如果写成必须参数会报错TypeError: var_args_dict() takes 1 positional argument but 3 were given
def var_args_tuple(arg1, *var_args):
    print(arg1, var_args)


def var_args_dict(arg1, **var_args):
    print(arg1, var_args)


sum_lambda: Callable[[Any, Any], Any] = lambda arg1, arg2: arg1 + arg2

# 全局变量
total = 0


def sum_total(arg1, arg2):
    total = arg1 + arg2
    print('局部变量total:', total)


helloworld()
print('width:', 3, 'heigth:', 4, 'area:', area(3, 4))
# 参数交换位置不影响结果
print('width:', 3, 'heigth:', 4, 'area:', area(height=4, width=3))
# 必须参数
welcome('小鸡鸡')
# 关键字参数
welcome(name='小鸡鸡')
# 默认参数an='dog'
animal('bone')
var_args_tuple(1, 2, 3)
var_args_dict(1, a=2, b=3)
sum_total(10, 20)
print('全局变量total：', total)
