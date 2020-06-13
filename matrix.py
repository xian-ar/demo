import pprint
r , c = (3,3)
a = []
for i in range(r):
    r = []
    for j in range(c):
        r.append(1)
    a.append(r)
    
pprint.pprint(a)
