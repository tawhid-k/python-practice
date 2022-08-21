
first = list(map(str, input().split(', ')))

d1 = dict()
d2 = dict()

for i in first:
    t = list(map(str, i.split(' : ')))
    d1[t[0]] = t[1]

for i in d1:
    lst = []
    for j in d1:
        if d1[i] == d1[j]:
            lst.append(j)
    d2[d1[i]] = lst
    
print(d2)