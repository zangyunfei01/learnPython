import unittest
import os
from learn_unittest.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(), 'test_case')
    testSuite = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='*test.py')

    with open('HTMLReport.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file,
                                title='Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(testSuite)
