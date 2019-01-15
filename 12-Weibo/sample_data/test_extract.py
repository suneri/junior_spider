import re
import sys

def test_get_variable():
    with open('post.html', 'r') as f:
        c = f.read()

    print(re.findall(r'var\s\$render_data\s=\s(\[[\s\S]*\])\[0\]\s\|\|\s\{\}\;', c)[0])

if __name__ == "__main__":
    for arg in sys.argv:
        print(arg)