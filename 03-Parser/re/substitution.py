# -*- coding: utf-8 -*-

import re

s = "The bigest 5 internet companies in China are Alibaba, Tencent, Baidu, JD and Toutiao."

re.sub(r'<?[A-Z][a-z]+?,\s>')

s1 = re.sub('China', 'USA', s)
print(re.sub(r'(?<=are\s)[\w,\s]+.', 'Apple, Amazon, Google, Facebook and Wikipedia', s1))