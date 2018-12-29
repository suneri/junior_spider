# -*- coding: utf-8 -*-

from lxml import html
from lxml import etree

import re

filename = 'Steve Jobs - Wikipedia.html'

with open(filename, 'r') as f:
    content = f.read()

tree = etree.HTML(content)

# Get Elements whose class name contains infobox
print( '--------------------------------------------')
print('Get Elements whose class name contains infobox')
print( '--------------------------------------------')
print( tree.xpath(u"//*[contains(@class, 'infobox')]"))
print( '')

# Get Elements whose class name contains infobox biography vcard
print( '--------------------------------------------')
print('Get Elements whose class name matches infobox biography vcard')
print( '--------------------------------------------')
print( tree.xpath(u"//*[@class='infobox biography vcard']"))
print( '')

# select element 1
print( '--------------------------------------------')
print('select element 1')
print( '--------------------------------------------')
print( tree.xpath(u"//table[contains(@class, 'infobox')][1]"))
print( '')

# Select child
print( '--------------------------------------------')
print('select child')
print( '--------------------------------------------')

print( tree.xpath(u"//table[contains(@class, 'infobox')][1]/tbody/tr"))
print( '')

# to string
print( '--------------------------------------------')
print('to string')
print( '--------------------------------------------')

print(etree.tostring(tree.xpath(u"//table[contains(@class, 'infobox')][1]/tbody/tr[2]")[0]))
print( "")

# get raw text by re
print( '--------------------------------------------')
print('get raw text by re')
print( '--------------------------------------------')

html_birth_element = etree.tostring(tree.xpath(u"//table[contains(@class, 'infobox')][1]/tbody/tr[2]")[0])
html_birth_element = html_birth_element.decode('utf8')

print(re.sub('<.*?>', '', html_birth_element))
print('')

pt_attrib = re.compile('<.*?>')

# iterate and get all infobox elements
print( '--------------------------------------------')
print('iterate and get all infobox elements')
print( '--------------------------------------------')
for element in tree.xpath(u"//table[contains(@class, 'infobox')][1]/tbody/tr"):
    try:
        thead = element.xpath('th')[0]
        s = etree.tostring(thead).decode('utf8')
        s = pt_attrib.sub('', s)
        print('Title:\t', s)
        tbody = element.xpath('td')[0]
        s = etree.tostring(tbody).decode('utf8')
        s = pt_attrib.sub('', s)
        print('Content:', s)
        print('')
    except Exception as err:
        pass