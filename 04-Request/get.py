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

with open("sina.html", "w+") as f:
    f.write(response.content.decode('utf8'))

# Here shows the incorrect encoding 
print(response.text)

print(response.encoding)

response.encoding = 'utf8'

print(response.text)

# Save the documents
with open("sina_b.html", "wb+") as f:
    f.write(response.content)

# Naming the files
fn1 = url[url.rfind('/')+1:]

# Save the documents
with open(fn1, "w+") as f:
    f.write(response.text)

fn2 = url[url.find('//')+2:]
fn2 = fn2.replace('/', '_')

# Save the documents
with open(fn2, "w+") as f:
    f.write(response.text)
