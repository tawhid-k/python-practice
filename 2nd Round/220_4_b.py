def printPattern(now, n):
    if now > n:
        return
    else:
        for i in range(now, n):
            print(end='  ')
        for i in range(1, now+1):
            print(i, end=' ')
        print()
    printPattern(now+1, n)
    

n = int(input())

printPattern(1,n)