#counter - dictionary of counts in a list/string
from collections import Counter

l = [1,1,1,1,1,12,2,2,2,2,2,2,2,3,333,4,4,4,4,4,5,5,5,5]
print(Counter(l))

s = 'asdadsklajslkdajlkdjdlkewdakjsd'
print(Counter(s))

s1 = 'How many times does each word show up in this sentence word word shoe up up'
words = s1.split()
print(Counter(s1.split()))

c = Counter(words)
print(c.most_common())
print(sum(c.values()))

n = 1
print(c.most_common()[:-n-1:-1]) #n least common elements