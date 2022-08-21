n, k = map(int, input().split())

arr = list(map(int, input().split()))
valid = 0
for i in arr:
    if 5 - i >= k:
        valid += 1
        
print(int(valid/3))