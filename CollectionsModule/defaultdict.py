from collections import defaultdict

#it will never raise a KeyError

d = {}
d1 = {'k1':1}

#d['one'] #raises KeyError

d = defaultdict(object)

print(d['one'])

d = defaultdict(lambda : 0)

print(d['one'])
print(d['two'])

for i in d:
    print(i)
for i in d.values():
    print(i)

