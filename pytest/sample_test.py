from sqlite3.dbapi2 import connect

import pytest
import time

"""
pytest.raises 抛出异常并捕获
用于有可预知异常的程序中，抛出并捕获异常，之后程序继续执行
"""


def test_raise():
    with pytest.raises(TypeError) as e:
        connect('localhost', '8080')
    exec_msg = e.value.args[0]
    assert exec_msg == 'must be real number, not str'


"""
@pytest.mark，给程序加上标签
执行时用 pytest -m，来筛选执行符合标签的程序

test_func1()和 test_func2()函数为例：
    筛选一个标记：
        pytest -m "finished"                                ————test_func1() 和 test_func2()均会被执行
    筛选多个标记：
        pytest -m "finished and commited"                   ————test_func1() 和 test_func2()均会被执行
        pytest -m "finished and commited and not merged"    ————test_func1()会被执行，test_func2()不会被执行
"""


@pytest.mark.finished
@pytest.mark.commited
@pytest.mark.merged
def test_func1():
    assert 1 == 1


@pytest.mark.finished
@pytest.mark.commited
@pytest.mark.unmerged
def test_func2():
    assert 2 == 2


"""
@pytest.mark.skip 标记函数
在执行时会被跳过，执行结果中会显示 skipped
"""


@pytest.mark.skip(reason='out-of-date api')
def test_connect():
    pass


"""
@pytest.mark.parametrize 参数化
接收两个参数
    1. 一个函数，一个标记，单个参数，第一个参数为程序中定义的参数名，str 类型，第二个参数为参数的值，放到一个 list 中
    2. 一个函数，一个标记，多个参数，第一个参数为程序中定义的参数名，str 类型，用","分隔，第二个参数为参数的值，放到一个 lit 中，同一组参数放到同一个 tuple 中
    3. 一个函数，多个标记，多个参数，形式同 1，但多个参数会进行笛卡尔组合，函数会执行 m x n 次
"""


@pytest.mark.parametrize("phone", [18800000001, 18800000008])
@pytest.mark.parametrize("captcha", [1, 12, 123, 1234])
def test_login(phone, captcha):
    print(phone, captcha)


@pytest.mark.parametrize("phone,captcha", [(18800000001, 1), (18800000001, 2)])
def test_login2(phone, captcha):
    print(phone, captcha)


"""
@pytest.fixture 固件
用于 test case 执行前后的预处理操作
预处理函数用 yield分割，case 执行前，预处理函数 yield 前的部分被执行；case 执行后，预处理函数 yield 后的部分被执行
"""


@pytest.fixture(scope="function")
def db():
    print('Connection esdablished')

    yield

    print('Connection closed')


def search_user(user_id):
    d = {
        '001': 'xiaoming'
    }
    return d[user_id]


def test_search(db):
    assert search_user('001') == 'xiaoming'


"""
scope，@pytest.fixture 的作用域，分 4 层，默认作用域为 function
    function: 函数级，每个测试函数都会执行一次固件；
       class: 类级别，每个测试类执行一次，所有方法都可以使用；
      module: 模块级，每个模块执行一次，模块内函数和方法都可使用；
     session: 会话级，一次测试只执行一次，所有被找到的函数和方法都可用。
"""
@pytest.fixture(scope='function')
def func_scope():
    pass


@pytest.fixture(scope='module')
def mod_scope():
    pass


@pytest.fixture(scope='session')
def sess_scope():
    pass


@pytest.fixture(scope='class')
def class_scope():
    pass

"""
fixture 作为测试函数参数传入，显式地调用不同作用域的 fixture
执行 pytest --setup-show  sample_test.py::test_multi_scope
可以看到执行顺序:

sample_test.py 
SETUP    S sess_scope
    SETUP    M mod_scope
        SETUP    F func_scope
        sample_test.py::test_multi_scope (fixtures used: func_scope, mod_scope, sess_scope).
        TEARDOWN F func_scope
    TEARDOWN M mod_scope
TEARDOWN S sess_scope

"""
def test_multi_scope(sess_scope, mod_scope, func_scope):
    pass


"""
对于类使用作用域，需要使用 pytest.mark.usefixtures （对函数和方法也适用）
执行 pytest --setup-show sample_test.py::TestClassScope
可以看到执行顺序：

sample_test.py 
      SETUP    C class_scope
        sample_test.py::TestClassScope::test_1 (fixtures used: class_scope).
        sample_test.py::TestClassScope::test_2 (fixtures used: class_scope).
      TEARDOWN C class_scope

"""
@pytest.mark.usefixtures('class_scope')
class TestClassScope:
    def test_1(self):
        pass

    def test_2(self):
        pass


"""
定义 fixture 的时候，添加 autouse 参数，可让测试函数自动调用 fixture
"""

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


@pytest.fixture(scope='session', autouse=True)
def timer_session_scope():
    start = time.time()
    print('\nstart: {}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))

    yield

    finished = time.time()
    print('finished: {}'.format(time.strftime(DATE_FORMAT, time.localtime(finished))))
    print('Total time cost: {:.3f}s'.format(finished - start))


@pytest.fixture(autouse=True)
def timer_function_scope():
    start = time.time()
    yield
    print(' Time cost: {:.3f}s'.format(time.time() - start))


def test_1():
    time.sleep(1)


def test_2():
    time.sleep(2)


"""
调用 fixture 的时候，fixture 的名字默认为定义的 fixture 名，通过 name 参数，可以重命名 fixture
"""

@pytest.fixture(name='age')
def calculate_average_age():
    return 28


def test_age(age):
    assert age == 28