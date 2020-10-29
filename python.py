import re

x = 1 + 2
b = type(x)

a = re.search('int|str|tuple|list|set',str(b))
print('Эта функция выводит тип объекта')


sqs = 0,1,4,9,16,25,36,49,64,81
print(sqs[7:5:-1])

v = 'asd'

print(v)
