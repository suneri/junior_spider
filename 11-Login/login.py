# -*- coding: utf-8 -*-

import requests
import os.path
import time

cookie_filename = 'cookie'

login_headers = {
    'origin': "http://localhost",
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "http://localhost/login/login.php",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'cache-control': "no-cache"
}

login_url = "http://localhost/login/login.php"

def dologin(username, password):
    payload = 'name={}&password={}'.format(username, password)

    response = requests.request("POST", login_url, headers=login_headers, 
    data=payload, allow_redirects=False)

    cookie = ''

    for k, v in response.cookies.iteritems():
        cookie += k + '=' + v + ';'
    cookie = cookie[:-1]

    with open(cookie_filename, 'w') as f:
        f.write(cookie)
    
    login_headers['cookie'] = cookie

def cookie_exist():
    return os.path.isfile(cookie_filename)

def cookie_valid():
    cookie_mid_time = os.path.getmtime(cookie_filename)
    return cookie_mid_time + 86400 * 2 > time.time()

def load_cookie():
    with open(cookie_filename, 'r') as f:
        cookie = f.read()
    login_headers['cookie'] = cookie
    return cookie

def login(username, password):
    # Check whether cookie is existed and valid
    if cookie_exist() and cookie_valid():
        cookie = load_cookie()
        return

    # Call login API, login and save cookie
    dologin(username, password)

if __name__ == "__main__":
    login('caca','c')
    print(login_headers)
    
    # res = requests.get('http://localhost/login/main.php', headers=login_headers)
    # print(res.text)