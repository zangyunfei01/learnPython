# 创建set可以用set函数，先创建一个list然后把list传入set中
L = [1, 2, 3, 4]
s = set(L)
print(s)

# 创建set也可以直接用{}，但是不能用{}直接创建空set，因为空的{}被创建dict占用了
d = {}
print(d)
s = {1, 2, 3, 4}
print(s)

# set中没有重复的元素，当向set中传入相同元素的时候，会过滤掉重复的元素
L = [1, 2, 3, 4, 4, 4]
s = set(L)
print(s)
print(len(s))

# set添加元素可以用add，如果元素已经存在，则不会添加到set中，add只可以添加单个元素
s.add(567)
print(s)
s.add(567)
print(s)

# 另一个添加元素的方法是update，可以同时添加多个元素，添加的时候也可以把list、tuple、dict当做参数传入
s.update('A', 'B', 'C')
print(s)
s.update(['L', 'M', 'N'], ('O', 'P', "Q"))
print(s)

# set删除元素用remove，如果是删除不存在的元素，用remove会报错。
s.remove(567)
print(s)

# 另一个删除元素的方法是discard，即使元素不存在时也不会报错
# s.remove(8)
s.discard(4)
print(s)
s.discard(3)
print(s)

# 随机删一个pop，每次打印结果可能不同
s.pop()
print(s)

# set集合元素个数用len()
print(len(s))

# 清空clear，清空后set中没有元素
s.clear()
print(s)
print(len(s))

# 删除set用del，删除后set就没有了，再print()会报错。用法和删除list、dict一样
del s
