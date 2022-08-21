t = int(input())
maxSum = 0
maxLst = []

for i in range(t):
    arr = list(map(int, input().split()))
    curSum = 0
    for j in arr:
        curSum += j
    if curSum > maxSum:
        maxSum = curSum
        maxLst = arr
        
print(maxSum)
print(maxLst)