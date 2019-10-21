import requests
import json
import time


def send_captcha():
    sign = 'f9bcbdde3586687596deae29d5c275e2'
    timestamp = int(time.time())
    data = {'phone': phone, 'sign': sign, 'timestamp': timestamp}
    header = {}
    r = requests.put('http://test-apis.520yidui.com/v2/auths/send_captcha.json', data=data, headers=header)
    if r.status_code < 400:
        print('发送成功')
    else:
        print('发送失败')
        exit()


def login(token, id):
    data = {'code': token, 'id': id}
    header = {}
    r = requests.post('http://test-apis.520yidui.com/v2/login', data=data, headers=header)
    if r.status_code < 400:
        response = json.loads(r.text)
        auth = response['token']
        print(auth)
    else:
        print(f'错误码:{r.status_code}')


def create(auth_id):
    print(auth_id)
    set_sex = input('请输入注册性别（男/女）：')
    if set_sex == '男':
        sex = 0
    elif set_sex == '女':
        sex = 1
    else:
        sex = 1
        # data = {"api_key": "7e08df24", "auth_id": auth_id, "channel_key": "market_QQ", "device_mac": "3C:A5:81:DD:C2:FD",
        #         "device_token": "McLGRRLQSfyZStlGRZMZo_QOytxFRKe551SOoRJQo5s45c+jR7JRoZe5j7Djy__4R1DGRtAjRKJQjcQjRcSv57JoRR+_jcMERKyOoK_FoZ54yKRW5FosFKp-QRL_j1SEj1MRjcMjj1QRRFosFKp-QRQGRkoR57AQR1MZy_k3Z7r-5HQvR1SoQQ5qF5cC-Vg8QzDZJzSjjcM_Q_eoVKg4y5+3FZF4yH_35KeFntRRRkRRoRDQQRDvQRMZRkRvQRM0",
        #         "education": 2, "marriage": 0,
        #         "member": {"birthday": "1995-01-01", "city_id": 0, "height": 170, "location_id": 1, "nickname": "坏坏的小刀",
        #         "member": {"birthday": "1995-01-01", "city_id": 0, "height": 170, "location_id": 1, "nickname": "坏坏的小刀",
        #                    "push_channel": "getui", "push_id": "", "sex": sex}, "salary": 3}

        data = {"auth_id": auth_id, "member[sex]": sex, "member[birthday]": "1995-01-01"}

    header = {'CodeTag': '6.7.2'}
    r = requests.post('http://test-apis.520yidui.com/v2/members/create', data=data, headers=header)
    response = json.loads(r.text)
    if r.status_code < 400:
        print(f'create状态码：{r.status_code}')
        login(response['token'], response['id'])
    else:
        print(f'错误码：{r.status_code}')
        print(response)
        exit()


def phone_auth(phone):
    send_captcha()
    captcha = input('请输入验证码：')
    data = {'phone': phone, 'captcha': captcha}
    header = {}
    r = requests.post('http://test-apis.520yidui.com/v2/auths/phone_auth', data=data, headers=header)
    if r.status_code < 400:
        response = json.loads(r.text)
        if 'auth_id' in response:
            create(response['auth_id'])
        else:
            login(response['token'], response['id'])
    else:
        print(f'错误码：{r.status_code}')


if __name__ == '__main__':
    phone = input('请输入手机号：')
    phone_auth(phone)
