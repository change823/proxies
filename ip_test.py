#-*-coding:utf-8-*-

import requests
url = 'http://www.instagram.com'

proxy = {
    "http": "3.211.17.212:80",
}

response = requests.get(url, proxies=proxy)
print(response.text)
