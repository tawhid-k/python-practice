def bubbleSort(arr):
  for i in range(len(arr)-1):
   for j in range(len(arr)-1-i):
    if arr[j] > arr[j+1]:
     arr[j], arr[j+1] = arr[j+1], arr[j]


first = list(map(str, input().split(', ')))

d1 = dict()

for i in first:
    t = list(map(str, i.split(': ')))
    d1[t[0]] = int(t[1])

first = list(map(str, input().split(', ')))

lst = []

for i in first:
    t = list(map(str, i.split(': ')))
    if t[0] in d1:
       d1[t[0]] += int(t[1])
    else:
        d1[t[0]] = int(t[1])

for i in d1:
    lst.append(d1[i])

bubbleSort(lst)
newlst = []

for i in lst:
    if i not in newlst:
        newlst.append(i)
    
mytuple = tuple(newlst)
print(d1)
print('Values: ',mytuple)
        
     