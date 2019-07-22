#!/usr/bin/env python3

# list
# python是动态语言，list中可以包含多种数据类型
from builtins import len

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


# list截取用：分割
# L[1:5]，取index为1 - 4位置上的元素，到5截止，不取5
# L[:5]，取从0 - 4位置上的元素，到5截止，不取5。从0开始0可以默认不写
# L[:]，取整个列表
# L[5:]，取index从5开始到结束的元素
# L[::5]，从index为0个元素开始取到最后，然后隔5个取1个
# L[4::5]，从index为4的元素开始取到最后，然后隔5个取一个
# L[4:20:5]，从index为4的元素开始取到index为20截止，不取index为20，然后隔5个取一个

# 元组截取同理

# 字符串截取同理
def first_char_upper(s):
    return s[:1].upper() + s[1:]  # 利用截取，把首字母和后面隔离出来，然后把首字母用upper方法转成大写，再与后面的拼接起来


print(first_char_upper('hello'))

# list 练习

# list用append方法直接在末尾添加元素
list2.append('Banana')
print(list2)

# list用extend()方法，将指定list'添加到本list中
list2.extend(list3)
print(list2)

# list用insert方法在指定位置添加元素
list2.insert(5, 'a~ ApplePen')
print(list2)

# list用remove方法，匹配列表中已有的元素并删除
# 如果没有这个元素，那就报错了 ValueError: list.remove(x): x not in list
list2.remove('Banana')
print(list2)

# list用pop方法删除指定位置元素。如果不指定位置，直接pop()，则是删除末位元素
list2.pop(0)

# 清空list中的元素，就变成空list，相当于del list[:]
# 而直接用del list，则是将list全部删除，再print的时候就报错了，因为list连个毛都没了
# list2.clear()
# del list2[:]
# del list2
print(list2)

# list用index，返回指定元素的索引位置
a = list2.index(1)
print(a)

# list用count，来统计指定元素出现的次数
b = list2.count(1)
print(b)

# list用sort，对list进行排序，当然，元素类型得相同，不同就会在run的时候报错了
# 直接print list.sort()会返回None，理解是list.sort()是排序过程，而不是生成一个新list，排序完后再print即是新排序后的结果
list4 = [2, 5, 4, 3, 1]
print(list4.sort())
list4.sort()
print(list4)

# list倒序用reverse，字面意思就是倒序，直接print list.reverse()也是会返回None的
list4.reverse()
print(list4.reverse())
print(list4)

# list的copy就是复制了，相当于list[:]
print(list4.copy())
print(list4[:])
print(list4.copy() == list4[:])
