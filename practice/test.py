import requests

url = "http://test-apis.520yidui.com/v2/members/geo_location"

payload = {'latitude': '28.2277800000',
           'longitude': '112.9388600000',
           'country': '中国',
           'province': '湖南',
           'city': '长沙'}
files = [

]
headers = {
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJpZCI6OTAzNzMsImV4cGlyZV9hdCI6IjIwMjAtMDMtMjMgMDE6NTA6MTQgKzA4MDAifQ.L5DaHew9Aon66MtJj6OrJIkD14_xSQ_deBDZvhNA3uM',
    'MemberId': 'fd716804f7d7b48bba0ecc887fd28d89'
}
response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
