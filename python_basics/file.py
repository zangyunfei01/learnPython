#!/usr/bin/python3


with open('/Users/zangyunfei/Desktop/test.txt', mode='w+') as file:
    count = file.write('python write')
    print(count)

with open('/Users/zangyunfei/Desktop/test.txt', mode='r+') as file:
    print(file.read())

