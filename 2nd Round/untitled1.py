arr = [-1 for i in range(10)]

def fun(n):
    global arr
    print(n)
    if arr[n] != -1:
        arr[n] = 5
        return arr[n]
    else:
        arr[n] = 5
        arr[n] = fun(n)
        return arr[n]
        
fun(5)