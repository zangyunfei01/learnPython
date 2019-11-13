#!/usr/bin/python3


with open('/Users/zangyunfei/Desktop/test.txt', mode='w+') as file:
    count = file.write(' file write \n file read \n input conut')
    print(count)

with open('/Users/zangyunfei/Desktop/test.txt', mode='r+') as file:
    # print(file.read())
    # print(file.readline())
    print(file.readlines())

