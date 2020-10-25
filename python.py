import re

x = 1 + 2
b = type(x)

a = re.search('int|str|tuple|list|set',str(b))


print(a.group(0))
