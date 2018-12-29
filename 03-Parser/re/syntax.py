# -*- coding: utf-8 -*-

import re

# s1 = "Boeing has unveiled its newest line of business jets, which the company says will allow VIP travelers to fly nonstop between any two cities on Earth."

s1 = "Boeing is a USA company. USA has many giant companies, including Boeing."

re.findall('^Boeing', s1)

re.findall('^USA', s1)

s2 = '<h3 class="LC20lb">map::find - C++ Reference - Cplusplus.com</h3>'

print(re.findall("class.", s2))

# None Greedy Mode
print(re.findall("Boe.+?\s", s1))

# Greedy Mode
print(re.findall("Boe.+\s", s1))

# Matching 0 or more
print(re.findall('Boe[a-z]*', s1))

# Matching 0 or 1
print(re.findall('Boe[a-z]*ng', s1))
# Compare with *
print(re.findall('Boe[a-z]?ng', s1))
# Matching 0 or 1
print(re.findall('Boe[a-z]*\s', s1))
# Compare with *
print(re.findall('Boe[a-z]?\s', s1))

print(re.findall("Boe[a-z]{1,2}\s", s1))
print(re.findall("Boe[a-z]{1,5}\s", s1))

s3 = "Huawei shipped more than 230 million mobile phones in global, a giant Chinese company."
print(re.findall(r"[^\d]+?\b", s3))
print(re.findall(r"\b([^\d]{5,8})\b", s3))
print(re.findall(r"\b[a-z]{5}\b", s3))