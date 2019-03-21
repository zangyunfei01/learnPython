#!/usr/bin/env python3

# list
# python是动态语言，list中可以包含多种数据类型

empty_list = []
list2 = [1, 2, 'what are you fucking say', True]
print(empty_list)
print(list2, "\nlist2的长度是", len(list2))

# 和java相同的地方，python中的list也是有序的，可以通过索引访问列表中的元素，索引从0开始
print(list2[0], list2[2])

# 超出索引会报数组越界异常:IndexError: list index out of range
# print(list2[4])

# list的倒序访问，用负号表示。虽然0表示正向第一位但是倒序第一位得用-1，-0的话是是个什么玩意
print(list2[-1])

# list添加元素的方法：append，末尾添加  insert，指定位置添加
list2.append('wonderful world')
print(list2)
list2.insert(2, 3)
list2.insert(3, 'wonderful day')
print(list2)

# list删除元素用pop：直接调用pop()，是删除末尾元素  pop(index)，是删除指定位置元素
list2.pop()
print(list2)
list2.pop(2)
print(list2)

# list替换元素：重新赋值
list2[1] = 'bibi'
print(list2)