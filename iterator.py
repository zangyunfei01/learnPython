#!/usr/bin/env python3

import sys

L = [1, 2, 3, 4]
iterator = iter(L)

# 用for循环遍历，循环输出变量x的值

# for x in iterator:
#     print(x, end=" ")

# 用while循环，用list长度规定循环次数，用next()方法打印出下一次遍历的值

# x = 0
# while x < len(L):
#     print(next(iterator), end=" ")
#     x += 1

# 用next()函数打印出下次遍历的值，用StopIteration 异常标识迭代的完成
while True:
    try:
        print(next(iterator), end=" ")
    except StopIteration:
        sys.exit()


