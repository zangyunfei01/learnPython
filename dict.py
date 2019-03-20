# dict 等同于java中的Map，键值对组成的集合
# dict 用{}表示，key和value用':'连接，key-value和key-value之间用','分隔

# 学号和学生姓名的dict
student = {1: 'Michael', 2: 'Bob', 3: 'Jerry'}

# dict 查询，通过key获取value，因此key不可以重复，多个key可以指向同一个value
print(student[1])

student = {1: 'Michael', 2: 'Bob', 3: 'Jerry', 4: 'Jerry'}
print(student)

# key可以是int类型，也可以是string，也可以是tuple类型。tuple类型一旦创建不能改变
student = {'Michael': 1}
print(student['Michael'])
num = {(1, 2, 3): 'Num'}
print(num)

# dict添加元素直接通过key给value赋值的形式添加
student = {1: 'Michael', 2: 'Bob', 3: 'Jerry', 4: 'Jerry'}
print(student)
student[5] = 'Apple'
print(student)

# dict更新元素也是通过key给value赋值的形式添加--对已有的key重新赋值
student[5] = 'Banana'
print(student)

# dict删除元素的方式也是通过key，去删除对应的key-value
# 删除元素的语法是del，然后想删什么直接删就行了
# 删除list、tuple或dict也一样
del student[5]
print(student)

del student
L = [1, 2, 3]
del L
t = ('A', 'B', 'C')
del t

#  遍历dict，同样地，遍历需要用到for。dict中key是唯一的，用for循环去遍历的时候其实是遍历的key，然后通过key找出对应的value
student = {1: 'Michael', 2: 'Bob', 3: 'Jerry', 4: 'Jerry', 5: 'Apple'}
for key in student:
    value = student[key]
    print(key, value)
