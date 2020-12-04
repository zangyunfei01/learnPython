import requests
import json
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4ddf5a8b-afae-4317-94e1-3736be33197b"
payload = {
    "msgtype": "text",
    "text": {
        "content": "到饭点儿了，该点餐了",
    }
}
headers = {
    'Content-Type': 'application/json'
}

payload = json.dumps(payload).encode("utf-8")
requests.request("POST",url,data=payload,headers=headers)