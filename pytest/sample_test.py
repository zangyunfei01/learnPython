import pytest



@pytest.mark.parametrize("phone", [18800000001, 18800000008])
@pytest.mark.parametrize("captcha", [1, 12, 123, 1234])
def test_login(phone, captcha):
    print(phone, captcha)


@pytest.mark.parametrize("phone,captcha", [(18800000001, 1), (18800000001, 2)])
def test_login2(phone, captcha):
    print(phone, captcha)


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



