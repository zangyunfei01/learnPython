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


def get_member_id():
    send_captcha()
    captcha = input('请输入验证码：\n')
    url = 'https://test-apis.520yidui.com/v2/auths/phone_auth'
    data = {'phone': phone, 'captcha': captcha}
    r = requests.post(url, data=data)
    if r.status_code < 400:
        response = json.loads(r.content)
        if 'auth_id' in response:
            r = create(response['auth_id'])
            id, token = r['id'], r['token']
            login(id, token)
            print(r['id'])
            return r['id']
        else:
            login(response['id'], response['token'])
            print(response['id'])
            return response['id']
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


def login(id, token):
    url = 'https://test-apis.520yidui.com/v2/login'
    data = {'id': id, 'code': token}
    r = requests.post(url, data=data)
    if r.status_code < 400:
        response = json.loads(r.content)
        auth = response['token']
        print(auth)
        return auth
    else:
        print(f'状态码:{r.status_code}')


def get_auth():
    url = 'https://test-apis.520yidui.com/v2/login'
    data = {'id': '0e5c5481909d1f9bcaafa60af5c6ef14',
            'code': 'ae227146eb5b2339d8f67ce51b63e00378aaf300d1deef2920cceabc246696f7'}
    r = requests.post(url, data=data)
    if r.status_code < 400:
        response = json.loads(r.content)
        auth = response['token']
        print(auth)
        return auth
    else:
        print(f'状态码:{r.status_code}')


if __name__ == '__main__':
    phone = input('请输入手机号：\n')
    get_member_id()
    # login()