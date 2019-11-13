

def output():
    print('{}网址：{}'.format('菜鸟教程', 'https://www.runoob.com'))
    print('{1}是{0}的网址'.format('菜鸟教程', 'https://www.runoob.com'))
    print('{b}网址：{a}'.format(b='菜鸟教程', a='https://www.runoob.com'))
    print('%s网址：%s,啦啦啦%d' % ('菜鸟教程', 'https://www.runnob.com', 123))


if __name__ == '__main__':
    input('请开始你的表演：')
    output()