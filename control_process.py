# python严格遵守缩进规则，具有相同缩进的代码构成代码块
# if的语法是if后面加语句，用:表示代码块开始，代码块要缩进写

score = 75
if score > 60:
    print('passed')

# if else需要分别在if语句最后，else后加：，if表达式的值为True，执行if代码块的语句，if表达式的值为False，执行else代码块的语句
score = 60
if score > 60:
    print('passed')
else:
    print('failed')

# else if 在python中简写成elif表示
score = 85
if score > 90:
    print('niubi')
elif 80 < score <= 90:
    print('haixing')
else:
    print('caibi')

# for ，java中的foreach的写法，遍历各种可以数据，即使是无序的，在python中也可以用for去遍历
L = [10, 20, 30, 40]
score = 0
for x in L:
    score = score + x
    print(score)
print('总分是：', score)

# while 同样是用：作为方法体开始的标识，然后方法体缩进写
# 打印一百以内的奇数和
sum_ji = 0
for x in range(0, 100):
    if x % 2 != 0:
        sum_ji = sum_ji + x
print('sum_ji:', sum_ji)

sum_ou = 0
x = 2
while x < 100:
    sum_ou = sum_ou + x
    x = x + 2
print('sum_ou:', sum_ou)

# break跳出循环，continue跳过当次循环继续下次循环

sum_test = 0
x = 2
while x < 100:
    if x == 98:
        break
    if x % 3 == 0:
        print(x)
        x = x + 1
    elif x % 3 != 0:
        x = x + 1
        continue