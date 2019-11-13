#!/usr/bin/env python3

import sys

"""
创建一个迭代器
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
更多内容查阅：Python3 面向对象
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
"""


class Numbers:
    def __iter__(self):
        self.init = 1
        return self

    def __next__(self):
        if self.init < 20:
            x = self.init
            self.init += 1
            return x
        else:
            raise StopIteration  # 这里当超限的时候用的是raise关键字和StopIteration异常来标识完成，raise关键字还没具体了解用法


numbers = Numbers()
iterator = iter(numbers)
print(next(iterator))

# 加上20次限制后就可以去遍历了
for i in numbers:
    print(i)

# 还有一个生成器，这里先拷贝定义和用法来，第一次没有看懂，以后用到的时候再深究，先把python常用部分学会，该开始函数了

"""
在 Python 中，使用了 yield 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象。

以下实例使用 yield 实现斐波那契数列：'''
"""


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()



