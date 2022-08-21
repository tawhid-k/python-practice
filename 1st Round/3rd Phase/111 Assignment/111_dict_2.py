d = dict()

while True:
    n = int(input())
    if n in d:
        d[n] += 1
    else:
        d[n] = 0

for i in d:
    print(str(i) + " - " + str(d[i]) + " times")