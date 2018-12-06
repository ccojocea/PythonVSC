# mg per 100g 
omega3_table = { "Salmon" : 2260, "Hering" : 1729, "Sardines" : 1480, "Flaxseeds" : 53400, "Eggs" : 400 } 


y = sorted(omega3_table, key=lambda x : omega3_table[x])
print(y)

z = sorted(omega3_table)
print(z)

w = sorted(omega3_table.values())
print(w)

print(list(map(lambda x: 2 + (0 if x==1 else 8),range(4))))