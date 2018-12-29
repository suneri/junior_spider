# -*- coding: utf-8 -*-

from lxml import html
from lxml import etree

import re


filename = 'Steve Jobs - Wikipedia.html'

with open(filename, 'r') as f:
    content = f.read()

print( '--------------------------------------------')
print( '# css selector' )
print( '--------------------------------------------')
htree = html.fromstring(content)
element = htree.cssselect('table.infobox.biography.vcard')[0]
print( '')

pt_attrib = re.compile('<.*?>')
pt_color = re.compile('\&.*?;')

# iterate and get all infobox elements
print( '--------------------------------------------')
print('iterate and get all infobox elements')
print( '--------------------------------------------')
for element in element.xpath("tbody/tr"):
    try:
        thead = element.xpath('th')[0]
        s = etree.tostring(thead).decode('utf8')
        s = pt_attrib.sub('', s)
        s = pt_color.sub('', s)
        print('Title:\t', s)
        tbody = element.xpath('td')[0]
        s = etree.tostring(tbody).decode('utf8')
        s = pt_attrib.sub('', s)
        s = pt_color.sub('', s)
        print('Content:', s)
        print('')
    except Exception as err:
        print(err)
        pass