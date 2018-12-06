from collections import OrderedDict

d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
d['g'] = 7
d['h'] = 8
d['i'] = 9

for k, v in d.items():
    print (k, v)

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
d['f'] = 'F'
d['g'] = 'G'
d['h'] = 'H'
d['i'] = 'I'

for k, v in d.items():
    print (k, v)

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['a'] = 2
d2['b'] = 1

print(d1 == d2)