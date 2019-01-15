# -*- coding: utf-8 -*-

from threading import Thread
import re
import requests
import os


class pic_downloader():
    res_dir = './res'
    
    def assure_res_dir(self):
        if not os.path.exists(self.res_dir):
            os.makedirs(self.res_dir)

    def get_media_files(self, pics):
        pic_urls = [x['large']['url'] for x in pics]
        t = Thread(target=self.download_pics, args=(pic_urls,))
        t.start()
        return pic_urls

    def download_pics(self, pic_urls):
        self.assure_res_dir()

        i = 1
        for url in pic_urls:
            print('Download picture', i, "of ", len(pic_urls))
            r = requests.get(url)
            filename = self.res_dir + url[url.rfind('/'):]
            with open(filename, 'wb') as f:
                f.write(r.content)
            i += 1