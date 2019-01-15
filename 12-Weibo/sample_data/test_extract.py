import re

with open('post.html', 'r') as f:
    c = f.read()

print(re.findall(r'var\s\$render_data\s=\s(\[[\s\S]*\])\[0\]\s\|\|\s\{\}\;', c)[0])