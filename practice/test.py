#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# # 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# # 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, "\n"\'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,\nLisa!'''
#
# print(n, '\n', f, '\n', s1, '\n', s2, '\n', s3, '\n', s4, '\n')
#
# r = 2.5
# s = 3.14 * r ** 2
# print(f'The area of a circle with radius {r} is {s:.2f}')
#
# s1 = 72
# s2 = 85
# r = (s2 - s1) / s1 * 100
# print('小明提升的百分点为：%.1f%%' % r)
#
# n1 = 255
# n2 = 1000
# print(hex(n1), hex(n2))
#
#
# def nop():
#     pass
#
#
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('你这类型不对，得是整形或小数才行')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
#
# print(my_abs(0))
#
# import math
#
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# r = move(100, 100, 60, math.pi / 6)
# print(r)
#
#
# def quadratic(a, b, c):
#     return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#
#
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')
#
#
# # 位置参数
# def power(x):
#     return x * x
#
#
# def power2(x, n):
#     while not isinstance(x, (int, float)) & isinstance(n, int):
#         raise TypeError('得是整形或浮点型才行')
#     else:
#         return x ** n
#
#
# # 默认值参数
# def power3(x, n=2):
#     while not isinstance(x, (int, float)) & isinstance(n, int):
#         raise TypeError('得是整形或浮点型才行')
#     else:
#         return x ** n
#
#
# print(power3(0.5))
#
#
# # 可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# num = [1, 2, 3]
# num2 = (1, 2, 3)
#
# print(calc(1, 2, 3, 4))
# print(calc(*num))
# print(calc(*num2))
#
#
# # 关键字参数
#
# def product(*args):
#     s = 1
#     if len(args) == 0:
#         raise TypeError
#     for x in args:
#         s = s * x
#     return s
#
#
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')
#
#
# # 去除字符串首尾的所有空格
# #    Hello
# def trim(s):
#     if s == "" or s == " ":
#         return ""
#     elif s[0] == " ":
#         s = s[1:]
#         return trim(s)
#     elif s[-1] == " ":
#         s = s[:-1]
#         return trim(s)
#     else:
#         return s
#
#
# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# print(trim("    hello    "))
# print(trim("a "))
# print(trim(""))
# print(trim(" "))
"""
len(L) == 10
range(len(L)) = [0,1,2,3,4,5,6,7,8,9]
x
"""

# def findMinAndMax(L):
#     min_L = max_L = 0
#     if len(L) == 0:
#         min_L = max_L = None
#     elif len(L) == 1:
#         min_L = max_L = L[0]
#     else:
#         for x in range(len(L) - 1):
#             if L[x] > L[x + 1]:
#                 temp = L[x]
#                 L[x] = L[x + 1]
#                 L[x + 1] = temp
#         min_L = L[0]
#         max_L = L[-1]
#     return min_L, max_L
#
#
# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([1, 1, 3, 5, 9, 7, 9]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')
#
# list_x = [x * x for x in range(1, 11)]
# print(list_x)
#
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() for x in L1 if isinstance(x, str)]
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')
#
# from functools import reduce
#
# L1 = ['adam', 'LISA', 'barT']
#
#
# def normalize(name):
#     return name[0].upper() + name[1:].lower()
#
#
# L2 = list(map(normalize, L1))
# print(L2)
#
# L = [1, 2, 3, 4, 5]
# print(sum(L))
#
#
# def prod(L):
#     def fn(x, y):
#         return x * y
#
#     return reduce(fn, L)
#
#
# print(prod(L))
#
# L = [1, 2, 4, 5, 6, 9, 10, 15]


# 结果: [1, 5, 9, 15]

# def odd_fillter(l):
#     def is_odd(n):
#         return n % 2 == 1
#
#     return list(filter(is_odd, l))
#
#
# print(odd_fillter(L))
#
#
# # 改成 lambda 函数形式
# def odd_filtter_lambda(l):
#     return list(filter(lambda n: n % 2 == 1, l))
#
#
# print(odd_filtter_lambda(L))
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
#
# def sort_by_name(l):
#     name = []
#     for x in l:
#         name.append(x[0])
#     # return sorted(name,reverse=True)
#     return list(reversed(name))
#
#
# print(sort_by_name(L))
#
#
# def create_counter():
#     count = 0
#
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#
#     return counter
#
#
# count = create_counter()
# print(count(), count())

# decorator
import time
import datetime

from pytz import timezone
from functools import wraps

#
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"call {func.__name__}")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# def log1(text):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print(f"called function:{func.__name__}")
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
#
#
# @log1("execute")
# def now():
#     tz = timezone('Asia/Shanghai')
#     t = datetime.datetime.fromtimestamp(int(time.time()), tz).strftime('%Y-%m-%d %H:%M:%S')
#     return t
#
# def timestmp():
#     return int(time.time())
#
#
# def metric(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print('%s executed in %s ms' % (fn.__name__, 10.24))
#         return fn(*args, **kwargs)
#
#     return wrapper
#
#
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
#
# def log2(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print("begin call function: %s" % fn.__name__)
#         fn(*args, **kwargs)
#         print("end call function: %s" % fn.__name__)
#         return
#
#     return wrapper
#
#
# def log3(fn_or_desc):
#     if type(fn_or_desc) == str:
#         def derocator(fn):
#             @wraps(fn)
#             def wrapper(*args, **kwargs):
#                 begin_time = timestmp()
#                 print("begin time: %s" % begin_time)
#                 print("begin call function: %s" % fn.__name__)
#                 fn(*args, **kwargs)
#                 time.sleep(2)
#                 end_time = timestmp()
#                 print("end call function: %s" % fn.__name__)
#                 print("end time: %s" % end_time)
#                 print("execuet time: %s" % (end_time-begin_time))
#
#             return wrapper
#
#         return derocator
#     else:
#         @wraps(fn_or_desc)
#         def wrapper(*args, **kwargs):
#             print("begin call function: %s" % fn_or_desc.__name__)
#             fn_or_desc(*args, **kwargs)
#             print("end call function: %s" % fn_or_desc.__name__)
#             return
#
#         return wrapper
#
#
# @log2
# def test2():
#     print("function name: %s" % test2.__name__)
#
#
# @log3
# def test3_1():
#     print("function name: %s" % test3_1.__name__)
#
#
# @log3("execute")
# def test3_2():
#     print("function name: %s" % test3_2.__name__)
#
#
# if __name__ == '__main__':
# print(now())
# print(now.__name__)
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# else:
#     print("测试成功")
# test2()
# test3_1()
# test3_2()

# # partial
# from functools import partial
#
#
# def int2(x):
#     return int(x, base=2)
#
#
# int8 = partial(int,base=8)
# max2 = partial(max,10)
#
#
# print(int("10000", base=10))
# print(int("10000", base=2))
# print(int8("10000"))
# print(max(5,6,7))
# print(max2(5,6,7))

# module
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'Invisible-AFEI'

# import sys
#
# def test():
#     args = sys.argv
#     print(args)
#     if len(args) == 1:
#         print('Hello, world!')
#     elif len(args) == 2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
#
# if __name__ == '__main__':
#     test()
#     print(sys.path)

# class Student(object):
#     """
#     Class ans Instance
#     """
#
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self, gender):
#         self.__gender = gender
#
#
# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# class Student(object):
#     pass
#     __slots__ = ("name", "__gender", "score")
# count = 0

# def __init__(self, name: str, gender: str):
#     self.name = name
#     self.__gender = gender
#     Student.count += 1

# def get_gender(self) -> str:
#     return self.__gender
#
# def set_gender(self, gender):
#     if gender in ("male", "female"):
#         self.__gender = gender
#     else:
#         raise ValueError("性别只接收 male 和 female")


# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     print(bart.count)
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# s = Student()
# s.name = ("WTF")
# s.gender = "male"
# s.__gender = "male"
# print(s.name)
# print(s.gender)

# class Student(object):
#     __author__ = "Invisible-AFEI"
#     __slots__ = ("name", "age", "score")
#
#     def __init(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_score(self):
#         return self.score
#
#     def set_score(self, value: int):
#         if not isinstance(value, int):
#             raise TypeError("socre只接收 int 类型值")
#         elif value < 0 or value > 100:
#             raise ValueError("score 只接收 0-100 范围的值")
#         else:
#             self.score = value
#             print("修改score 为：%s" % value)
#
#
# s = Student()
# s.name = "Michael"
# print(s.name)
# s.age = 19
# print("%s 的年龄是 %s" % (s.name, s.age))
# # s.gender = "male"
#
# s.set_score(60)
#
# s.set_score("aha")
#
# s.set_score(101)
#
#
# class Screen(object):
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self,value):
#         self._height = value
#
#     @property
#     def resolution(self):
#         return self.height * self.width
#
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')


# from enum import Enum
#
# Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun'))
#
# print(Month.Jan.value)
#
#
# import requests
# import json
# import jwt
#
#
# def get_auth():
#     URL = "https://api.520yidui.com"
#     PHONE_AUTH = "/v2/auths/phone_auth"
#     LOGIN = "/v3/login"
#     PHONE = "18310061886"
#     CAPTCHA = "1886"
#     phone_auth_data = {
#         "phone": PHONE,
#         "captcha": CAPTCHA
#     }
#     phone_auth = requests.post(url=URL + PHONE_AUTH, data=phone_auth_data)
#     id = json.loads(phone_auth.content)["id"]
#     token = json.loads(phone_auth.content)["token"]
#     login_data = {
#         "id": id,
#         "code": token
#
#     }
#     login = requests.post(url=URL + LOGIN, data=login_data)
#     auth = json.loads(login.content)["token"]
#     return auth
#
#
# print(get_auth())
#
#
# def test(n):
#     if n != "":
#         print("true")
#     else:
#         print("false")
#
#
# test(0)

#
# from functools import reduce
# import logging
# logging.basicConfig(level=logging.INFO)
#
# def str2num(s):
#     if '.' in s:
#         return float(s)
#     else:
#         return int(s)
#
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
#
# def main():
#     try:
#         r = calc('100 + 200 + 345')
#         print('100 + 200 + 345 =', r)
#         r = calc('99 + 88 + 7.6')
#         print('99 + 88 + 7.6 =', r)
#     except Exception as e:
#         # print(e)
#         logging.exception(e)
#
#
# print('BEGIN')
# main()
# print('END')

# import unittest
# import logging
# logging.basicConfig(level=logging.INFO)
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         # logging.exception(type(self.score))
#
#     def get_grade(self):
#         # if type(self.score) == int:
#         if isinstance(self.score, int):
#             if 80 <= self.score <= 100:
#                 return 'A'
#             elif 60 <= self.score < 80:
#                 return 'B'
#             elif 0 <= self.score < 60:
#                 return 'C'
#             else:
#                 raise ValueError
#         else:
#             raise TypeError
#
# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid_value(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
#     def test_invalid_type(self):
#         s1 = Student('Bart', 'abc')
#         s2 = Student('Lisa', 'xyz')
#         with self.assertRaises(TypeError):
#             s1.get_grade()
#         with self.assertRaises(TypeError):
#             s2.get_grade()
#
#
# if __name__ == '__main__':
#     unittest.main()


# def fact(n):
#     '''
#     Calculate 1*2*...*n
#
#     >>> fact(1)
#     1
#     >>> fact(10)
#     3628800
#     >>> fact(-1)
#     Traceback (most recent call last):
#       File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/doctest.py", line 1329, in __run
#         exec(compile(example.source, filename, "single",
#       File "<doctest __main__.fact[2]>", line 1, in <module>
#         fact(-1)
#       File "/Users/zangyunfei/workspace/learnPython/practice/test.py", line 778, in fact
#         raise ValueError()
#     ValueError
#     '''
#     if n < 1:
#         raise ValueError()
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()

# path = '/Users/zangyunfei/Desktop/model.yaml'

# f = open(path, 'r')
# f.read()
# f.close()
# f = open(path, 'w+')
# f.write('Hello, world2!')
# f.close()
# print(f.readline())
# print(f.readlines())
# for x in f.readlines():
#     print(x.strip())
# with open(path, 'r') as f:
#     print(f.read())
# with open(path, 'r+') as f:
#     f.write('hello, afei')
# with open(path,'r') as f:
#     print(f.readline())
# with open(path,'r') as f:
#     print(f.readlines())
# with open(path, 'w') as f:
#     f.write('Hello, AFEI !')
# with open(path, 'w+') as f:
#     print(f.read())
# with open(path, 'w+') as f:
#     f.write('Hello, AFEI !\n')
# with open(path, 'a') as f:
#     f.write('Hello, AFEI !')
# with open(path, 'a+') as  f:
#     print(f.read())

# from io import StringIO, BytesIO
#
# s = StringIO('Hello!\nHi!\nGoodBye!')
# print(s)
# # print(s.read())
# # print(s.readline())
# print(s.readlines())
#
# b = BytesIO('中文'.encode('utf-8'))
# print(b)
# # print(b.read())
# # print(b.readline())
# print(b.readlines())
#
# print('中文'.encode('utf-8'))

import os

# print(os.name)
# print(os.uname())
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))
# test_dir = os.path.join('/Users/zangyunfei/workspace/learnPython/practice', 'test_dir')
# os.rmdir(test_dir)
# os.mkdir(test_dir)
# print(os.path.split('/Users/zangyunfei/workspace/learnPython/practice'))
# print(type(test_dir))
# import os
#
# for x in os.listdir('.'):
#     # print(x)
#     print(os.path.join('/Users/zangyunfei/workspace/learnPython/practice', x))
# file_name = []
# for x in os.walk('.'):
#     if x not in file_name:
#         file_name.append(x)
# print(file_name)

# d = dict(name='Bob', age=20, score=88)
# print(d)

# headers = {
#     'auth1': 'adb',
#     'auth2': 'def'
# }
# # h = dict((k, v) for k, v in headers.items() if v != "")
# # print(h)
# d = dict((k, v) for k, v in headers.items())
# l = [(k,v) for k,v in headers.items()]
# g = ((k,v) for k,v in headers.items())
# print(d)
# print(l)
# print(g)

# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

import json
import requests

# webhook发送企业微信通知
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=13dbe1f8-a283-4ce5-b279-16e541655d04"
data = {
    "msgtype": "text",
    "text": {
        "content": "广州今日天气：29度，大部分多云，降雨概率：60%",
        "mentioned_list": ["zangyunfei", "@all"],
        "mentioned_mobile_list": ["18310061886", "@all"]
    }
}

requests.post(url, data=data)  # !/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# # 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# # 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, "\n"\'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,\nLisa!'''
#
# print(n, '\n', f, '\n', s1, '\n', s2, '\n', s3, '\n', s4, '\n')
#
# r = 2.5
# s = 3.14 * r ** 2
# print(f'The area of a circle with radius {r} is {s:.2f}')
#
# s1 = 72
# s2 = 85
# r = (s2 - s1) / s1 * 100
# print('小明提升的百分点为：%.1f%%' % r)
#
# n1 = 255
# n2 = 1000
# print(hex(n1), hex(n2))
#
#
# def nop():
#     pass
#
#
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('你这类型不对，得是整形或小数才行')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
#
# print(my_abs(0))
#
# import math
#
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# r = move(100, 100, 60, math.pi / 6)
# print(r)
#
#
# def quadratic(a, b, c):
#     return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#
#
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')
#
#
# # 位置参数
# def power(x):
#     return x * x
#
#
# def power2(x, n):
#     while not isinstance(x, (int, float)) & isinstance(n, int):
#         raise TypeError('得是整形或浮点型才行')
#     else:
#         return x ** n
#
#
# # 默认值参数
# def power3(x, n=2):
#     while not isinstance(x, (int, float)) & isinstance(n, int):
#         raise TypeError('得是整形或浮点型才行')
#     else:
#         return x ** n
#
#
# print(power3(0.5))
#
#
# # 可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# num = [1, 2, 3]
# num2 = (1, 2, 3)
#
# print(calc(1, 2, 3, 4))
# print(calc(*num))
# print(calc(*num2))
#
#
# # 关键字参数
#
# def product(*args):
#     s = 1
#     if len(args) == 0:
#         raise TypeError
#     for x in args:
#         s = s * x
#     return s
#
#
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')
#
#
# # 去除字符串首尾的所有空格
# #    Hello
# def trim(s):
#     if s == "" or s == " ":
#         return ""
#     elif s[0] == " ":
#         s = s[1:]
#         return trim(s)
#     elif s[-1] == " ":
#         s = s[:-1]
#         return trim(s)
#     else:
#         return s
#
#
# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# print(trim("    hello    "))
# print(trim("a "))
# print(trim(""))
# print(trim(" "))
"""
len(L) == 10
range(len(L)) = [0,1,2,3,4,5,6,7,8,9]
x
"""

# def findMinAndMax(L):
#     min_L = max_L = 0
#     if len(L) == 0:
#         min_L = max_L = None
#     elif len(L) == 1:
#         min_L = max_L = L[0]
#     else:
#         for x in range(len(L) - 1):
#             if L[x] > L[x + 1]:
#                 temp = L[x]
#                 L[x] = L[x + 1]
#                 L[x + 1] = temp
#         min_L = L[0]
#         max_L = L[-1]
#     return min_L, max_L
#
#
# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([1, 1, 3, 5, 9, 7, 9]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')
#
# list_x = [x * x for x in range(1, 11)]
# print(list_x)
#
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() for x in L1 if isinstance(x, str)]
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')
#
# from functools import reduce
#
# L1 = ['adam', 'LISA', 'barT']
#
#
# def normalize(name):
#     return name[0].upper() + name[1:].lower()
#
#
# L2 = list(map(normalize, L1))
# print(L2)
#
# L = [1, 2, 3, 4, 5]
# print(sum(L))
#
#
# def prod(L):
#     def fn(x, y):
#         return x * y
#
#     return reduce(fn, L)
#
#
# print(prod(L))
#
# L = [1, 2, 4, 5, 6, 9, 10, 15]


# 结果: [1, 5, 9, 15]

# def odd_fillter(l):
#     def is_odd(n):
#         return n % 2 == 1
#
#     return list(filter(is_odd, l))
#
#
# print(odd_fillter(L))
#
#
# # 改成 lambda 函数形式
# def odd_filtter_lambda(l):
#     return list(filter(lambda n: n % 2 == 1, l))
#
#
# print(odd_filtter_lambda(L))
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
#
# def sort_by_name(l):
#     name = []
#     for x in l:
#         name.append(x[0])
#     # return sorted(name,reverse=True)
#     return list(reversed(name))
#
#
# print(sort_by_name(L))
#
#
# def create_counter():
#     count = 0
#
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#
#     return counter
#
#
# count = create_counter()
# print(count(), count())

# decorator
import time
import datetime

from pytz import timezone
from functools import wraps

#
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"call {func.__name__}")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# def log1(text):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print(f"called function:{func.__name__}")
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
#
#
# @log1("execute")
# def now():
#     tz = timezone('Asia/Shanghai')
#     t = datetime.datetime.fromtimestamp(int(time.time()), tz).strftime('%Y-%m-%d %H:%M:%S')
#     return t
#
# def timestmp():
#     return int(time.time())
#
#
# def metric(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print('%s executed in %s ms' % (fn.__name__, 10.24))
#         return fn(*args, **kwargs)
#
#     return wrapper
#
#
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
#
# def log2(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print("begin call function: %s" % fn.__name__)
#         fn(*args, **kwargs)
#         print("end call function: %s" % fn.__name__)
#         return
#
#     return wrapper
#
#
# def log3(fn_or_desc):
#     if type(fn_or_desc) == str:
#         def derocator(fn):
#             @wraps(fn)
#             def wrapper(*args, **kwargs):
#                 begin_time = timestmp()
#                 print("begin time: %s" % begin_time)
#                 print("begin call function: %s" % fn.__name__)
#                 fn(*args, **kwargs)
#                 time.sleep(2)
#                 end_time = timestmp()
#                 print("end call function: %s" % fn.__name__)
#                 print("end time: %s" % end_time)
#                 print("execuet time: %s" % (end_time-begin_time))
#
#             return wrapper
#
#         return derocator
#     else:
#         @wraps(fn_or_desc)
#         def wrapper(*args, **kwargs):
#             print("begin call function: %s" % fn_or_desc.__name__)
#             fn_or_desc(*args, **kwargs)
#             print("end call function: %s" % fn_or_desc.__name__)
#             return
#
#         return wrapper
#
#
# @log2
# def test2():
#     print("function name: %s" % test2.__name__)
#
#
# @log3
# def test3_1():
#     print("function name: %s" % test3_1.__name__)
#
#
# @log3("execute")
# def test3_2():
#     print("function name: %s" % test3_2.__name__)
#
#
# if __name__ == '__main__':
# print(now())
# print(now.__name__)
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# else:
#     print("测试成功")
# test2()
# test3_1()
# test3_2()

# # partial
# from functools import partial
#
#
# def int2(x):
#     return int(x, base=2)
#
#
# int8 = partial(int,base=8)
# max2 = partial(max,10)
#
#
# print(int("10000", base=10))
# print(int("10000", base=2))
# print(int8("10000"))
# print(max(5,6,7))
# print(max2(5,6,7))

# module
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'Invisible-AFEI'

# import sys
#
# def test():
#     args = sys.argv
#     print(args)
#     if len(args) == 1:
#         print('Hello, world!')
#     elif len(args) == 2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
#
# if __name__ == '__main__':
#     test()
#     print(sys.path)

# class Student(object):
#     """
#     Class ans Instance
#     """
#
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self, gender):
#         self.__gender = gender
#
#
# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# class Student(object):
#     pass
#     __slots__ = ("name", "__gender", "score")
# count = 0

# def __init__(self, name: str, gender: str):
#     self.name = name
#     self.__gender = gender
#     Student.count += 1

# def get_gender(self) -> str:
#     return self.__gender
#
# def set_gender(self, gender):
#     if gender in ("male", "female"):
#         self.__gender = gender
#     else:
#         raise ValueError("性别只接收 male 和 female")


# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     print(bart.count)
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# s = Student()
# s.name = ("WTF")
# s.gender = "male"
# s.__gender = "male"
# print(s.name)
# print(s.gender)

# class Student(object):
#     __author__ = "Invisible-AFEI"
#     __slots__ = ("name", "age", "score")
#
#     def __init(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_score(self):
#         return self.score
#
#     def set_score(self, value: int):
#         if not isinstance(value, int):
#             raise TypeError("socre只接收 int 类型值")
#         elif value < 0 or value > 100:
#             raise ValueError("score 只接收 0-100 范围的值")
#         else:
#             self.score = value
#             print("修改score 为：%s" % value)
#
#
# s = Student()
# s.name = "Michael"
# print(s.name)
# s.age = 19
# print("%s 的年龄是 %s" % (s.name, s.age))
# # s.gender = "male"
#
# s.set_score(60)
#
# s.set_score("aha")
#
# s.set_score(101)
#
#
# class Screen(object):
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self,value):
#         self._height = value
#
#     @property
#     def resolution(self):
#         return self.height * self.width
#
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')


# from enum import Enum
#
# Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun'))
#
# print(Month.Jan.value)
#
#
# import requests
# import json
# import jwt
#
#
# def get_auth():
#     URL = "https://api.520yidui.com"
#     PHONE_AUTH = "/v2/auths/phone_auth"
#     LOGIN = "/v3/login"
#     PHONE = "18310061886"
#     CAPTCHA = "1886"
#     phone_auth_data = {
#         "phone": PHONE,
#         "captcha": CAPTCHA
#     }
#     phone_auth = requests.post(url=URL + PHONE_AUTH, data=phone_auth_data)
#     id = json.loads(phone_auth.content)["id"]
#     token = json.loads(phone_auth.content)["token"]
#     login_data = {
#         "id": id,
#         "code": token
#
#     }
#     login = requests.post(url=URL + LOGIN, data=login_data)
#     auth = json.loads(login.content)["token"]
#     return auth
#
#
# print(get_auth())
#
#
# def test(n):
#     if n != "":
#         print("true")
#     else:
#         print("false")
#
#
# test(0)

#
# from functools import reduce
# import logging
# logging.basicConfig(level=logging.INFO)
#
# def str2num(s):
#     if '.' in s:
#         return float(s)
#     else:
#         return int(s)
#
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
#
# def main():
#     try:
#         r = calc('100 + 200 + 345')
#         print('100 + 200 + 345 =', r)
#         r = calc('99 + 88 + 7.6')
#         print('99 + 88 + 7.6 =', r)
#     except Exception as e:
#         # print(e)
#         logging.exception(e)
#
#
# print('BEGIN')
# main()
# print('END')

# import unittest
# import logging
# logging.basicConfig(level=logging.INFO)
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         # logging.exception(type(self.score))
#
#     def get_grade(self):
#         # if type(self.score) == int:
#         if isinstance(self.score, int):
#             if 80 <= self.score <= 100:
#                 return 'A'
#             elif 60 <= self.score < 80:
#                 return 'B'
#             elif 0 <= self.score < 60:
#                 return 'C'
#             else:
#                 raise ValueError
#         else:
#             raise TypeError
#
# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid_value(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
#     def test_invalid_type(self):
#         s1 = Student('Bart', 'abc')
#         s2 = Student('Lisa', 'xyz')
#         with self.assertRaises(TypeError):
#             s1.get_grade()
#         with self.assertRaises(TypeError):
#             s2.get_grade()
#
#
# if __name__ == '__main__':
#     unittest.main()


# def fact(n):
#     '''
#     Calculate 1*2*...*n
#
#     >>> fact(1)
#     1
#     >>> fact(10)
#     3628800
#     >>> fact(-1)
#     Traceback (most recent call last):
#       File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/doctest.py", line 1329, in __run
#         exec(compile(example.source, filename, "single",
#       File "<doctest __main__.fact[2]>", line 1, in <module>
#         fact(-1)
#       File "/Users/zangyunfei/workspace/learnPython/practice/test.py", line 778, in fact
#         raise ValueError()
#     ValueError
#     '''
#     if n < 1:
#         raise ValueError()
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()

# path = '/Users/zangyunfei/Desktop/model.yaml'

# f = open(path, 'r')
# f.read()
# f.close()
# f = open(path, 'w+')
# f.write('Hello, world2!')
# f.close()
# print(f.readline())
# print(f.readlines())
# for x in f.readlines():
#     print(x.strip())
# with open(path, 'r') as f:
#     print(f.read())
# with open(path, 'r+') as f:
#     f.write('hello, afei')
# with open(path,'r') as f:
#     print(f.readline())
# with open(path,'r') as f:
#     print(f.readlines())
# with open(path, 'w') as f:
#     f.write('Hello, AFEI !')
# with open(path, 'w+') as f:
#     print(f.read())
# with open(path, 'w+') as f:
#     f.write('Hello, AFEI !\n')
# with open(path, 'a') as f:
#     f.write('Hello, AFEI !')
# with open(path, 'a+') as  f:
#     print(f.read())

# from io import StringIO, BytesIO
#
# s = StringIO('Hello!\nHi!\nGoodBye!')
# print(s)
# # print(s.read())
# # print(s.readline())
# print(s.readlines())
#
# b = BytesIO('中文'.encode('utf-8'))
# print(b)
# # print(b.read())
# # print(b.readline())
# print(b.readlines())
#
# print('中文'.encode('utf-8'))

import os

# print(os.name)
# print(os.uname())
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))
# test_dir = os.path.join('/Users/zangyunfei/workspace/learnPython/practice', 'test_dir')
# os.rmdir(test_dir)
# os.mkdir(test_dir)
# print(os.path.split('/Users/zangyunfei/workspace/learnPython/practice'))
# print(type(test_dir))
# import os
#
# for x in os.listdir('.'):
#     # print(x)
#     print(os.path.join('/Users/zangyunfei/workspace/learnPython/practice', x))
# file_name = []
# for x in os.walk('.'):
#     if x not in file_name:
#         file_name.append(x)
# print(file_name)

# d = dict(name='Bob', age=20, score=88)
# print(d)

# headers = {
#     'auth1': 'adb',
#     'auth2': 'def'
# }
# # h = dict((k, v) for k, v in headers.items() if v != "")
# # print(h)
# d = dict((k, v) for k, v in headers.items())
# l = [(k,v) for k,v in headers.items()]
# g = ((k,v) for k,v in headers.items())
# print(d)
# print(l)
# print(g)

# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
import jwt
import json

# jwt decode
jwt_token = "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6ODgxODQsImV4cGlyZV9hdCI6IjIwMjAtMTItMDUgMjM6Mzg6NTUgKzA4MDAifQ.zuc80pNPtYetu2ZbBxgQnZROMTfqm-bF2BNLQrLJd9s"
data = json.dumps(jwt.decode(jwt=jwt_token, key='', verify=False, algorithms=['HS256']))
print(data)
#
# # jwt encode
# payload = {"id": 28271028, "expire_at": "2020-12-12 14:25:53 +0800"}
# token = jwt.encode(payload=payload, key='', algorithm='HS256').decode('utf-8')
# print(token)
#
# # # 批量生成 token，并写入 auth.csv
# with open('/Users/zangyunfei/Desktop/id.csv', 'r') as ids:
#     for id in ids.readlines():
#         payload = {"id": int(id.strip()), "expire_at": "2022-12-22 22:22:22 +0800"}
#         token = jwt.encode(payload=payload, key='', algorithm='HS256').decode('utf-8')
#         with open('/Users/zangyunfei/Desktop/auth.csv', 'a') as jwt_token:
#             jwt_token.write(token)
#             jwt_token.write('\n')
# with open('/Users/zangyunfei/Desktop/auth.csv', 'r') as jwt_token:
#     print(jwt_token.readline())


# meta_datas = [
#     [
#         {
#             "name": "v3校验手机号",
#             "data": [
#                 {
#                     "request": {
#                         "url": "https://test1-api.520yidui.com/v3/auths/phone_auth",
#                         "method": "POST",
#                         "headers": "{\n  \"User-Agent\":\"python-requests/2.24.0\",\n  \"Accept-Encoding\":\"gzip, deflate\",\n  \"Accept\":\"*/*\",\n  \"Connection\":\"keep-alive\",\n  \"Content-Type\":\"application/json\",\n  \"Content-Length\":\"43\"\n}",
#                         "body": "{\n  &#34;phone&#34;: &#34;16600000004&#34;,\n  &#34;captcha&#34;: &#34;1234&#34;\n}"
#                     },
#                     "response": {
#                         "ok": True,
#                         "url": "https://test1-api.520yidui.com/v3/auths/phone_auth",
#                         "status_code": 200,
#                         "reason": "OK",
#                         "cookies": "{}",
#                         "encoding": "utf-8",
#                         "headers": "{\n  \"Date\":\"Tue, 01 Dec 2020 10:01:29 GMT\",\n  \"Content-Type\":\"application/json; charset=utf-8\",\n  \"Content-Length\":\"458\",\n  \"Connection\":\"keep-alive\",\n  \"Content-Encoding\":\"gzip\",\n  \"Vary\":\"Accept-Encoding\",\n  \"Access-Control-Allow-Origin\":\"*\",\n  \"Access-Control-Allow-Credentials\":\"true\",\n  \"Access-Control-Allow-Methods\":\"GET, POST, PUT, DELETE, OPTIONS\",\n  \"Access-Control-Allow-Headers\":\"Memberid,Codetag,Channel,Accept,Authorization,Cache-Control,Content-Type,DNT,If-Modified-Since,Keep-Alive,Origin,User-Agent,X-Requested-With\"\n}",
#                         "content_type": "application/json; charset=utf-8",
#                         "body": "{\n  \"action\":\"login\",\n  \"age\":23,\n  \"avatar\":{\n    \"status\":0,\n    \"url\":\"https://img.520yidui.com/uploads/member_avatar/avatar/93031/2b34ce505f879ca2eb99f193aa814e69.jpg@!normal\"\n  },\n  \"bucket_action_id\":null,\n  \"consume_rose_count\":99,\n  \"first_paid_at\":0,\n  \"id\":\"84d043ea32eb3fc5e66baa167744d6ab\",\n  \"is_matchmaker\":false,\n  \"is_vip\":true,\n  \"location_id\":12,\n  \"nickname\":\"我们最英俊\",\n  \"phone_validate\":true,\n  \"register_app_id\":1,\n  \"register_at\":1593404499,\n  \"rose_count\":99620083,\n  \"sex\":0,\n  \"token\":\"3abb2005bfdc7ebeba686ff9c71a32e2e8a2d978ce480e98fc176a4e3d3e8bda\",\n  \"unionid\":\"oIRQzwtrLDyq46FdoGuDO4EanKVc_del_2019-08-08 21:18:08 +0800\",\n  \"vip\":true\n}"
#                     }
#                 }
#             ],
#             "stat": {
#                 "response_time_ms": 64.93,
#                 "elapsed_ms": 62.893,
#                 "content_size": 604
#             },
#             "validators": {
#                 "validate_extractor": [
#                     {
#                         "comparator": "equals",
#                         "check": "status_code",
#                         "check_value": 200,
#                         "expect": 200,
#                         "expect_value": 200,
#                         "check_result": "pass"
#                     }
#                 ]
#             }
#         }
#     ],
#     {
#         "name": "v2登录",
#         "data": [
#             {
#                 "request": {
#                     "url": "https://test1-api.520yidui.com/v2/login",
#                     "method": "POST",
#                     "headers": "{\n  \"User-Agent\":\"python-requests/2.24.0\",\n  \"Accept-Encoding\":\"gzip, deflate\",\n  \"Accept\":\"*/*\",\n  \"Connection\":\"keep-alive\",\n  \"Content-Type\":\"application/json\",\n  \"CODETAG\":\"yidui-9.9.9\",\n  \"Content-Length\":\"118\"\n}",
#                     "body": "{\n  &#34;code&#34;: &#34;3abb2005bfdc7ebeba686ff9c71a32e2e8a2d978ce480e98fc176a4e3d3e8bda&#34;,\n  &#34;id&#34;: &#34;84d043ea32eb3fc5e66baa167744d6ab&#34;\n}"
#                 },
#                 "response": {
#                     "ok": True,
#                     "url": "https://test1-api.520yidui.com/v2/login",
#                     "status_code": 201,
#                     "reason": "Created",
#                     "cookies": "{}",
#                     "encoding": "None",
#                     "headers": "{\n  \"Date\":\"Tue, 01 Dec 2020 10:01:29 GMT\",\n  \"Content-Type\":\"application/json\",\n  \"Content-Length\":\"273\",\n  \"Connection\":\"keep-alive\",\n  \"ETag\":\"W/\\\"2d041baad4d75f78742494f18301648f\\\"\",\n  \"Cache-Control\":\"max-age=0, private, must-revalidate\",\n  \"X-Request-Id\":\"d92e0e23a38d88fa90c15144b8dbbece\",\n  \"X-Runtime\":\"0.004938\",\n  \"Access-Control-Allow-Origin\":\"*\",\n  \"Access-Control-Allow-Credentials\":\"true\",\n  \"Access-Control-Allow-Methods\":\"GET, POST, PUT, DELETE, OPTIONS\",\n  \"Access-Control-Allow-Headers\":\"Memberid,Codetag,Channel,Accept,Authorization,Cache-Control,Content-Type,DNT,If-Modified-Since,Keep-Alive,Origin,User-Agent,X-Requested-With\"\n}",
#                     "content_type": "application/json",
#                     "body": "{\n  \"token\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OTMwMzEsImV4cGlyZV9hdCI6IjIwMjAtMTItMDEgMjA6MDE6MjkgKzA4MDAiLCJkZXZpY2VfaWQiOm51bGwsImdpb2lkIjpudWxsLCJ5ZGlkIjpudWxsLCJjaGFubmVsX25hbWUiOm51bGwsImlwIjoiMzYuMTEwLjg2LjIwMyJ9.2M9Qdcdv3r2rjRTjMcmPt54kGn5Zr1mhkByO-OUE7H8\"\n}"
#                 }
#             }
#         ],
#         "stat": {
#             "response_time_ms": 54.95,
#             "elapsed_ms": 52.912,
#             "content_size": 273
#         },
#         "validators": {
#             "validate_extractor": [
#                 {
#                     "comparator": "equals",
#                     "check": "status_code",
#                     "check_value": 201,
#                     "expect": 201,
#                     "expect_value": 201,
#                     "check_result": "pass"
#                 }
#             ]
#         }
#     }
# ]
#
# for z in meta_datas:
#     if isinstance(z, list):
#         continue
#     elif isinstance(z, dict):
#         data = z["data"]
# print(data)

# import time
# t = str(time.time()).split('.')[0]
# print(type(t))
# print(t)

# error = "\u4eca\u65e5\u5934\u50cf\u4e0a\u4f20\u6b21\u6570\u5df2\u7ecf\u8fbe\u5230\u4e0a\u9650"
# print(type(error))
# print(error.encode('utf-8'))
# print(type(error.encode('utf-8')))
# error = error.encode('utf-8').decode('utf-8')
# print(error)


# meta_datas = [
#     [
#         [
#             {
#                 "name": "v3校验手机号",
#                 "data": [
#                     {
#                         "request": {
#                             "url": "https://test1-api.520yidui.com/v3/auths/phone_auth",
#                             "method": "POST",
#                             "headers": "{\n  \"User-Agent\":\"python-requests/2.24.0\",\n  \"Accept-Encoding\":\"gzip, deflate\",\n  \"Accept\":\"*/*\",\n  \"Connection\":\"keep-alive\",\n  \"Channel\":\"market_GUANWANG\",\n  \"CodeTag\":\"yidui-9.9.9\",\n  \"timestamp\":\"1608000309\",\n  \"noncestr\":\"lekxsmmiclwqwhnlzazmzxirrphxinhc\",\n  \"Content-Type\":\"application/json\",\n  \"Content-Length\":\"43\"\n}",
#                             "body": "{\n  &#34;phone&#34;: &#34;16600000004&#34;,\n  &#34;captcha&#34;: &#34;1234&#34;\n}"
#                         },
#                         "response": {
#                             "ok": True,
#                             "url": "https://test1-api.520yidui.com/v3/auths/phone_auth",
#                             "status_code": 200,
#                             "reason": "OK",
#                             "cookies": "{}",
#                             "encoding": "utf-8",
#                             "headers": "{\n  \"content-encoding\":\"gzip\",\n  \"content-type\":\"application/json; charset=utf-8\",\n  \"vary\":\"Accept-Encoding\",\n  \"date\":\"Tue, 15 Dec 2020 02:45:09 GMT\",\n  \"content-length\":\"458\",\n  \"x-envoy-upstream-service-time\":\"7\",\n  \"server\":\"istio-envoy\"\n}",
#                             "content_type": "application/json; charset=utf-8",
#                             "body": "{\n  \"action\":\"login\",\n  \"age\":23,\n  \"avatar\":{\n    \"status\":0,\n    \"url\":\"https://img.520yidui.com/uploads/member_avatar/avatar/93031/2b34ce505f879ca2eb99f193aa814e69.jpg@!normal\"\n  },\n  \"bucket_action_id\":null,\n  \"consume_rose_count\":99,\n  \"first_paid_at\":0,\n  \"id\":\"84d043ea32eb3fc5e66baa167744d6ab\",\n  \"is_matchmaker\":false,\n  \"is_vip\":true,\n  \"location_id\":12,\n  \"nickname\":\"我们最英俊\",\n  \"phone_validate\":true,\n  \"register_app_id\":1,\n  \"register_at\":1593404499,\n  \"rose_count\":99612951,\n  \"sex\":0,\n  \"token\":\"3abb2005bfdc7ebeba686ff9c71a32e2e8a2d978ce480e98fc176a4e3d3e8bda\",\n  \"unionid\":\"oIRQzwtrLDyq46FdoGuDO4EanKVc_del_2019-08-08 21:18:08 +0800\",\n  \"vip\":true\n}"
#                         }
#                     }
#                 ],
#                 "stat": {
#                     "response_time_ms": 100.73,
#                     "elapsed_ms": 98.77,
#                     "content_size": 604
#                 },
#                 "validators": {
#                     "validate_extractor": [
#                         {
#                             "comparator": "equals",
#                             "check": "status_code",
#                             "check_value": 200,
#                             "expect": 200,
#                             "expect_value": 200,
#                             "check_result": "pass"
#                         }
#                     ]
#                 }
#             }
#         ],
#         {
#             "name": "v2登录",
#             "data": [
#                 {
#                     "request": {
#                         "url": "https://test1-api.520yidui.com/v2/login",
#                         "method": "POST",
#                         "headers": "{\n  \"User-Agent\":\"python-requests/2.24.0\",\n  \"Accept-Encoding\":\"gzip, deflate\",\n  \"Accept\":\"*/*\",\n  \"Connection\":\"keep-alive\",\n  \"Content-Type\":\"application/json\",\n  \"CODETAG\":\"yidui-9.9.9\",\n  \"Content-Length\":\"118\"\n}",
#                         "body": "{\n  &#34;code&#34;: &#34;3abb2005bfdc7ebeba686ff9c71a32e2e8a2d978ce480e98fc176a4e3d3e8bda&#34;,\n  &#34;id&#34;: &#34;84d043ea32eb3fc5e66baa167744d6ab&#34;\n}"
#                     },
#                     "response": {
#                         "ok": True,
#                         "url": "https://test1-api.520yidui.com/v2/login",
#                         "status_code": 201,
#                         "reason": "Created",
#                         "cookies": "{}",
#                         "encoding": "None",
#                         "headers": "{\n  \"content-type\":\"application/json\",\n  \"etag\":\"W/\\\"a9746cd98f47778e862c5715cd9a2e0d\\\"\",\n  \"cache-control\":\"max-age=0, private, must-revalidate\",\n  \"x-request-id\":\"5bbb1037-8316-942a-a26b-e221fbaa45f7\",\n  \"x-runtime\":\"0.005128\",\n  \"content-length\":\"273\",\n  \"x-envoy-upstream-service-time\":\"6\",\n  \"date\":\"Tue, 15 Dec 2020 02:45:09 GMT\",\n  \"server\":\"istio-envoy\"\n}",
#                         "content_type": "application/json",
#                         "body": "{\n  \"token\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OTMwMzEsImV4cGlyZV9hdCI6IjIwMjAtMTItMTUgMTI6NDU6MDkgKzA4MDAiLCJkZXZpY2VfaWQiOm51bGwsImdpb2lkIjpudWxsLCJ5ZGlkIjpudWxsLCJjaGFubmVsX25hbWUiOm51bGwsImlwIjoiMzYuMTEwLjg2LjIwMiJ9.zew0uWYAKKEtd74wNdR5z2ltpyws22iavp18YcOrdP4\"\n}"
#                     }
#                 }
#             ],
#             "stat": {
#                 "response_time_ms": 87.84,
#                 "elapsed_ms": 85.781,
#                 "content_size": 273
#             },
#             "validators": {
#                 "validate_extractor": [
#                     {
#                         "comparator": "equals",
#                         "check": "status_code",
#                         "check_value": 201,
#                         "expect": 201,
#                         "expect_value": 201,
#                         "check_result": "pass"
#                     }
#                 ]
#             }
#         }
#     ],
#     {
#         "name": "互动通知",
#         "data": [
#             {
#                 "request": {
#                     "url": "https://test1-api.520yidui.com/v3/chats/notification",
#                     "method": "GET",
#                     "headers": "{\n  \"User-Agent\":\"python-requests/2.24.0\",\n  \"Accept-Encoding\":\"gzip, deflate\",\n  \"Accept\":\"*/*\",\n  \"Connection\":\"keep-alive\",\n  \"Authorization\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OTMwMzEsImV4cGlyZV9hdCI6IjIwMjAtMTItMTUgMTI6NDU6MDkgKzA4MDAiLCJkZXZpY2VfaWQiOm51bGwsImdpb2lkIjpudWxsLCJ5ZGlkIjpudWxsLCJjaGFubmVsX25hbWUiOm51bGwsImlwIjoiMzYuMTEwLjg2LjIwMiJ9.zew0uWYAKKEtd74wNdR5z2ltpyws22iavp18YcOrdP4\"\n}"
#                 },
#                 "response": {
#                     "ok": False,
#                     "url": "https://test1-api.520yidui.com/v3/chats/notification",
#                     "status_code": 500,
#                     "reason": "Internal Server Error",
#                     "cookies": "{}",
#                     "encoding": "utf-8",
#                     "headers": "{\n  \"content-encoding\":\"gzip\",\n  \"content-type\":\"application/json; charset=utf-8\",\n  \"vary\":\"Accept-Encoding\",\n  \"date\":\"Tue, 15 Dec 2020 02:45:09 GMT\",\n  \"content-length\":\"26\",\n  \"x-envoy-upstream-service-time\":\"1\",\n  \"server\":\"istio-envoy\"\n}",
#                     "content_type": "application/json; charset=utf-8",
#                     "body": "[]"
#                 }
#             }
#         ],
#         "stat": {
#             "response_time_ms": 132.51,
#             "elapsed_ms": 130.413,
#             "content_size": 2
#         },
#         "validators": {
#             "validate_extractor": [
#                 {
#                     "comparator": "equals",
#                     "check": "status_code",
#                     "check_value": 500,
#                     "expect": 200,
#                     "expect_value": 200,
#                     "check_result": "fail"
#                 }
#             ]
#         }
#     }
# ]


# def traverse_list(l:list):
#     for x in l:
#         if isinstance(x,list):
#             return traverse_list(x)
#         else:
#             return x
#
# print(traverse_list(meta_datas)["data"])

import pytest
import requests

base_url = "https://test1-api.520yidui.com"


def phone_auth(phone, captcha):
    path = "/v3/auths/phone_auth"
    data = {
        "phone": phone,
        "captcha": captcha
    }
    headers = {}

    r = requests.post(url=base_url + path, data=data, headers=headers)
    print(r.json())
    print(r.status_code)
    # return r.json()
    return r.status_code


phone_auth(18800000008, 1234)
