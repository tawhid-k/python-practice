arr = [-1] * 1000

def dp (n):
    global arr
    if n == 0:
        return 0
    elif arr[n] != -1:
        return arr[n]
    else:
        s = str(n)
        minVal = dp(n-int(s[0]))
        for i in s:
           minVal = min(minVal, dp(n-int(i)))
        arr[n] = minVal
        return arr[n]
n = int(input())
print(dp(n))
