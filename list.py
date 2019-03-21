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

# 列表的长度用len()函数
print(len(list2))

# 列表中元素最大最小值用max()和min()
# 这里给list2用max()和min()会报错，因为list2中包含不同类型数据，无法进行大小比较
# TypeError: '>' not supported between instances of 'str' and 'int'

list3 = [1, 2, 3, 4]
print(max(list3), min(list3))

# 这应该是比较的字母在ASCII码中对应的值
list4 = ['Apple', 'Banana', 'Orange', '1']
print(max(list4), min(list4))

# 将tuple转化为list，只需要把list作为函数名，tuple作为参数传入即可
t = (1, 2, 3)
print(list(t))