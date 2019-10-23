import requests
import json
import time


def send_captcha():
    url = 'https://test-apis.520yidui.com/v2/auths/send_captcha'
    timestamp = time.time()
    data = {'sign': 'c5f6a3e950ad0223332de376c0608741', 'timestamp': timestamp, 'phone': phone}
    r = requests.put(url, data=data)
    if r.status_code < 400:
        print('发送成功')
    else:
        print('发送失败')


def get_headers():
    send_captcha()
    captcha = input('请输入验证码：\n')
    url = 'https://test-apis.520yidui.com/v2/auths/phone_auth'
    data = {'phone': phone, 'captcha': captcha}
    r = requests.post(url, data=data)
    if r.status_code < 400:
        response = json.loads(r.content)
        if 'auth_id' in response:
            auth_id = response['auth_id']
            print('auth_id:', auth_id)
            create(auth_id)
            id, code = create(auth_id)['id'], create(auth_id)['token']
            headers = {'Authorization': login(id, code)['token'], 'MemberId': create(auth_id)}
            print('Headers:', headers)
            return headers
        else:
            id, code = response['id'], response['token']
            headers = {'Authorization': login(id, code)['token'], 'MemberId': id}
            print('Headers:', headers)
            return headers
    else:
        print(f'状态码：{r.status_code}')


def get_headers_by_test_count(phone, captcha):
    url = 'https://test-apis.520yidui.com/v2/auths/phone_auth'
    data = {'phone': phone, 'captcha': captcha}
    r = requests.post(url, data=data)
    if r.status_code < 400:
        response = json.loads(r.content)
        id, code = response['id'], response['token']
        headers = {'Authorization': login(id, code)['token'], 'MemberId': id}
        print('Headers:', headers)
        return headers
    else:
        print(f'状态码：{r.status_code}')


def create(auth_id):
    url = 'https://test-apis.520yidui.com/v2/members/create'
    sex = input('请输入性别（0代表男，1代表女）:\n')
    bitrh = input('请输入生日（xx-xx-xx)：\n')
    data = {'auth_id': auth_id, 'member[sex]': sex, 'member[birthday]': bitrh,
            'channel_key': 'market_miUI'}
    headers = {'CodeTag': 'yidui-6.8.0',
               'DeviceToken': 'Zzehsc_lRRs1RN7uSVB1sj_9DNxlswJfSfFaewStsfRN3zy1DWdlD45hSWS13PD13zDKSNAwSWgP3P_kSzshDWBuDj5c3zBlSV5zS4RNsWolswsaSNo13z5asWg9Szok3fr7SfFzJWs7SzBhsVF9SW_usz57SnocszB1GvMhGW5lsWDSSfFP3fF1RoBmBwQ9GCS9ifekSORCR1RXSzB1QcDRvfBhJjDkGwJwD4rmBVZwDbQmewDtENo9S9oc3zgcJWehJWB1S9ohJWM0'}
    r = requests.post(url, data=data, headers=headers)
    return json.loads(r.content)


def login(id, code):
    url = 'https://test-apis.520yidui.com/v2/login'
    data = {'id': id, 'code': code}
    r = requests.post(url, data=data)
    if r.status_code < 400:
        print('登录成功')
        return json.loads(r.content)
    else:
        print(f'状态码:{r.status_code}')


if __name__ == '__main__':
    phone = input('请输入手机号：\n')
    get_headers()
    get_headers_by_test_count('18700000001', '123456')
