# encoding=utf-8

import unittest


class mytest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        "初始化类固件"
        print("----setUpClass")

    @classmethod
    def tearDownClass(cls):
        "重构类固件"
        print("----tearDownClass")

    # 初始化工作
    def setUp(self):
        self.a = 3
        self.b = 1
        print("--setUp")

    # 具体的测试用例，一定要以test开头
    def test_1(self):
        # 断言两数之和的结果是否是4
        print('1')

    def test_2(self):
        # 断言两数之差的结果是否是2
        try:
            self.assertTrue(1 == 2)
        except AssertionError as e:
            print(e)

    @unittest.skip('skipping')
    def test_3(self):
        # 断言两数之差的结果是否是2
        print('3')


if __name__ == '__main__':

    suite1 = unittest.TestLoader().loadTestsFromTestCase(mytest)
    suites = unittest.TestSuite(suite1)
    unittest.TextTestRunner(verbosity=2).run(suites)
