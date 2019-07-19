L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
balabala
# 打印apple
print(L[0][0])
# print python
print(L[1][1])


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def power2(x2, n2):
    if n2 > 0:
        return x2 ** n2


print(power(2, 3))
print(power2(2, 3))
