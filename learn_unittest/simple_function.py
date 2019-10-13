# encoding=utf-8

import unittest
import random


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.sequence = range(10)
        print('setUp sucess!')

    def tearDown(self):
        print('tearDown done!')

    def test_run(self):
        element = random.choice(self.sequence)
        self.assertTrue(element in self.sequence)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def test_shuffle(self):
        # 随机打乱原seq的顺序
        random.shuffle(self.seq)
        print(self.seq)
        self.seq.sort()
        print(self.seq)
        self.assertEqual(self.seq, list(range(10)))
        # 验证执行函数时抛出了TypeError异常
        # 直接执行radom.shuffle((1, 2, 3))时会报TypeError: 'tuple' object does not support item assignment
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


if __name__ == '__main__':
    unittest.main()
