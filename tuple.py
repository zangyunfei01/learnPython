#!/usr/bin/env python3

# python中另一种有序列表：tuple，称之为元组。
# tuple与list写法不同之处是创建时存放元素用()替代了[]，但是访问时仍要用[]，因为访问时[]是用来放index的

t = (1, 2, 3, 4)

# 错误的调用
# print(t(0)) → TypeError: 'tuple' object is not callable

# 正确的调用
print(t[0])
print(t)

# tuple一旦创建，tuple中的元素就无法改变，可以使用索引访问tuple中的元素，但是不能像list那样使用添加、删除、替换方法

# 错误的方法使用
# t.pop(3) → AttributeError: 'tuple' object has no attribute 'pop'

# 创建空列表
t = ()
print(t)

# tuple只有1个元素时，需要在元素后加上一个','以表示这个是tuple。不加的话()会表示运算时的优先级，会提示()多余并引导删除
t = (1)
print(t)
t = (1,)
print(t)

# tuple 和 list 的嵌套

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

L3 = [9, L1, 10, t1]
t3 = (9, L2, 10, t2)
print(L3)
print(t3)