# -*- coding: utf-8 -*-

from threading import Thread
import re
import requests

class pic_downloader():
    def get_media_files(self, html_doc):
        pic_urls = re.findall(r'<img.*\ssrc="(//att.newsmth.net/nForum/att/.*?)"', html_doc)
        t = Thread(target=self.download_pics, args=(pic_urls,))
        t.start()

    def download_pics(self, urls):
        for url in pic_urls:
            url = 'http:' + url
            r = requests.get(url)
            filename = re.findall(r'nForum/att/(.*)', url)[0].replace('/', '_') + '.jpg'
            with open(filename, 'wb') as f:
                f.write(r.content)

if __name__ == "__main__":
    with open('smth.html', 'r') as f:
        c = f.read()
    pic_downloader().get_media_files(c)