testcase = int(input())

for test in range(testcase):
    n = int(input())
    arr = list(map(int, input().split()))
    d = dict()
    for i in range(n):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    isVal = True
    for i in d:
        if d[i] == 1:
            isVal = False
            break
    if isVal == False:
        print('-1')
    else:
        idx = 0
        for i in d:
            f = d[i]
            going = idx
            idx += f
            print(idx, end=' ')
            for j in range(f-1):
                print(going+j, end=' ')
        print()