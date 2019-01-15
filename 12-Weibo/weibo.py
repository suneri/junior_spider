import requests
import os
import json
import re
import time
from pic_downloader import pic_downloader
import datetime
from mysql_manager import MysqlManager
import sys

class WeiboCrawler():

    cookie_filename = 'cookie'

    data_dir = './data'

    login_url = "https://passport.weibo.cn/sso/login"

    payload = "username={}&password={}&savestate=1&mainpageflag=1&entry=mweibo&ec=0".format('18600663368', 'Xi@oxiang66')
    
    login_headers = {
        'origin': "https://passport.weibo.cn",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "*/*",
        'referer': "https://passport.weibo.cn/signin/login",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        'cache-control': "no-cache"
    }

    post_url = 'https://m.weibo.cn/detail/{}'
    reply_url_0 = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id_type=0'
    reply_url_1 = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id={}&max_id_type=0'

    comments = []

    pattern = re.compile('<.*?>')

    def __init__(self, limit = 500 ):
        self.reply_limit = limit
        self.mm = MysqlManager(4)

    def cookie_exist(self):
        return os.path.isfile(self.cookie_filename)

    def cookie_valid(self):
        cookie_mid_time = os.path.getmtime(self.cookie_filename)
        return cookie_mid_time + 86400 * 2 > time.time()

    def load_cookie(self):
        with open(self.cookie_filename, 'r') as f:
            cookie = f.read()
        self.login_headers['cookie'] = cookie
        return cookie

    def do_login(self):
        response = requests.post(self.login_url, data=self.payload, headers=self.login_headers, allow_redirects=False)

        cookie = ''

        for k, v in response.cookies.iteritems():
            cookie += k + '=' + v + ';'
        cookie = cookie[:-1]

        with open(self.cookie_filename, 'w') as f:
            f.write(cookie)
        
        login_headers['cookie'] = cookie
    
    def login(self):
        # Check whether cookie is existed and valid
        if self.cookie_exist() and self.cookie_valid():
            cookie = self.load_cookie()
            return

        # Call login API, login and save cookie
        self.do_login()

    def assure_data_dir(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def cleanup_text(self, text):
        return self.pattern.sub('', text)

    def save_data(self, filename, data):
        self.assure_data_dir()
        with open(self.data_dir + '/{}.json'.format(filename), 'w') as f:
            f.write(data)

    def extract_var(self, html):
        return re.findall(r'var\s\$render_data\s=\s(\[[\s\S]*\])\[0\]\s\|\|\s\{\}\;', html)[0]

    # Wed Jan 16 00:00:52 +0800 2019
    # 2019-01-16 00:00:52
    def convert_time_format(self, ts):
        return datetime.datetime.strptime(ts, "%a %b %d %H:%M:%S %z %Y").strftime('%Y-%m-%d %H:%M:%S')

    def get_post(self, id):
        url = self.post_url.format(id)
        response = requests.get(url, headers=self.login_headers)
        post_data_str = self.extract_var(response.text)
        post_data = json.loads(post_data_str)[0]['status']

        self.post = {}

        print(post_data['created_at'])
        print(self.convert_time_format(post_data['created_at']))

        self.post['id'] = post_data['id']
        self.post['created_at'] = self.convert_time_format(post_data['created_at'])
        self.post['text'] = self.cleanup_text(post_data['text'])
        self.post['reposts_count'] = post_data['reposts_count']
        self.post['comments_count'] = post_data['comments_count']
        self.post['attitudes_count'] = post_data['attitudes_count']
        post_data_user = post_data['user']
        self.post['profile_image_url'] = post_data_user['profile_image_url']
        self.post['user_id'] = post_data_user['id']
        self.post['screen_name'] = post_data_user['screen_name']
        self.save_data( self.post['id'], post_data_str)
        self.mm.insert_data('post', self.post)

        post_pics = pic_downloader().get_media_files(post_data['pics'])
        for pic in post_pics:
            p = {}
            p['post_id'] = id
            p['url'] = pic
            self.mm.insert_data('pic', p)
    
    def get_comments(self, id, max_id):
        if max_id == 0:
            url = self.reply_url_0.format(id, id)
        else:
            url = self.reply_url_1.format(id, id, max_id)

        response = requests.get(url, headers=self.login_headers)
        reply_json_obj = json.loads(response.text)

        reply_data = reply_json_obj['data']['data']

        comment = {}

        for r in reply_data:
            comment['created_at'] = self.convert_time_format(r['created_at'])
            comment['id'] = r['id']
            comment['post_id'] = id
            comment['text'] = self.cleanup_text(r['text'])
            r_data_user = r['user']
            comment['profile_image_url'] = r_data_user['profile_image_url']
            comment['user_id'] = r_data_user['id']
            comment['screen_name'] = r_data_user['screen_name']
            self.comments.append(comment)
            self.mm.insert_data('comment', comment)

        self.save_data( self.post['id'] + '-{}'.format(max_id), response.text)
        
        if len(self.comments) >= reply_json_obj['data']['total_number']:
            return 

        if self.reply_limit is not 0 and len(self.comments) > int(self.reply_limit):
            return

        time.sleep(2)
        self.get_comments(self.post['id'], reply_json_obj['data']['max_id'])
        

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Must specify Weibo Feed ID")
        exit(0)

    limit = 100
    arg_len = len(sys.argv)

    if arg_len > 2:
        limit = sys.argv[2]
    id = sys.argv[1]

    wb_crawler = WeiboCrawler(limit)
    wb_crawler.login()
    wb_crawler.get_post(id)
    wb_crawler.get_comments(id, 0)