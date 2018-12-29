# -*- coding: utf-8 -*-

from lxml import html
from lxml import etree

import re

filename = 'Steve Jobs - Wikipedia.html'

with open(filename, 'r') as f:
    content = f.read()

tree = etree.HTML(content)

body_text_element = tree.xpath("//*[@id='bodyContent']//*[self::p or self::h2 or self::h3]")
pt_attrib = re.compile('<.*?>')

for ele in body_text_element:
    s = etree.tostring(ele).decode('utf8')
    s = pt_attrib.sub('', s)
    print(s)

# See attributes
body_text_element[10].xpath('a')[0].attrib