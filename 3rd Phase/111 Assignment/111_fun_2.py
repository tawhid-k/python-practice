def fun(minVal, maxVal, d):
    sum = 0
    for i in range(minVal, maxVal):
        if i % d == 0:
            sum += i
    print(sum)

n = input().replace('(', '')
n = n.replace(')', '')

n = n.split(', ')

minVal = int(n[0])
maxVal = int(n[1])
d = int(n[2])
fun(minVal, maxVal, d)

