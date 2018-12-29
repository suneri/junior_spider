# -*- coding: utf-8 -*-

# Documentation: https://docs.python.org/3/library/re.html

import re

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m.group(0)       # The entire match

m.group(1)       # The first parenthesized subgroup.

m.group(2)       # The second parenthesized subgroup.

m.group(1, 2)    # Multiple arguments give us a tuple.

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")

m.group('first_name')

m.group('last_name')

m = re.match(r"(\d+)\.(\d+)", "24.1632")
m.groups()