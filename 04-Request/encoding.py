# -*- coding: utf-8 -*-

import requests
import time

url = 'https://news.sina.com.cn/c/2018-12-10/doc-ihprknvu0188659.shtml'

headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'cache-control': "no-cache"
}

response = requests.get(url, headers = headers )

# Here shows the raw data with default encoding
print(response.content.decode('utf8'))

# Here shows string with requests' default encoding
print(response.text)

# Show the encoding used by requests
print(response.encoding)

# Change the encoding to utf8
response.encoding = 'utf8'

print(response.text)