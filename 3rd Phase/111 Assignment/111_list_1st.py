numbers = []

while True:
    val = input()
    if val == 'STOP':
        break
    else:
        n = int(val)
        numbers.append(n)

thisset = set()
for i in numbers:
    thisset.add(i)
for i in thisset:
    count = 0
    for j in numbers:
        if i == j:
            count += 1
    print(str(i) + " - " + str(count) + " times")