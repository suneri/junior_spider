# -*- coding: utf-8 -*-

# Documentation: https://docs.python.org/3/library/re.html

import re

s1 = '<h3 class="LC20lb">map::find - C++ Reference - Cplusplus.com</h3>'

prog = re.compile('C\+\+\s[^<]*')

result = prog.search(s1)

print(result)

s2 = 'David Beckham is a soccer star'

prog = re.compile('[A-Za-z\s]*')

result = prog.match(s2)

print(result)

result = prog.fullmatch(s2)

print(result)

s3 = 'Bob lives at Los Angles[1], has 2 publications[2][21]'

prog = re.compile('\[\d+\]')