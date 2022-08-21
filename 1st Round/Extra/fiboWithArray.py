arr = [-1] * 102

def fibo(n):
    if n < 2:
        arr[n] = 1
        return arr[n]
    elif arr[n] != -1:
        return arr[n]
    else:
        arr[n] = (fibo(n-1) + fibo(n-2))
        return arr[n]
    
fibo(100)

for i in range(0, 100):
    print(arr[i], end = ' ')