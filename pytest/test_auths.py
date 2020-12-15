import requests

class Test_phone_auth(object):
    base_url = "https://test1-api.520yidui.com"

    def phone_auth(self, phone, captcha):
        path = "/v3/auths/phone_auth"
        data = {
            "phone": phone,
            "captcha": captcha
        }
        r = requests.post(url=self.base_url + path, data=data)
        return r

    def test_phone_auth(self):
        phone_auth = self.phone_auth(18800000008,1234)
        assert phone_auth.status_code == 200
        assert phone_auth.json()["id"] == "a18e3a241d89a4d3b10e7466e448e406"
        assert phone_auth.json()["token"] == "2f06cab6ddb845f4dca0cd0b62cb0edf142a27f079d28b49cc2d244cbe0fcfaf"