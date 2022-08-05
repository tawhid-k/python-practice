ans = []

def bubbleSort(arr):
  sorted = True
  for i in range(len(arr)-1):
      if arr[i] > arr[i+1]:
          sorted = False
          break
  if sorted == True:
      return
  for i in range(len(arr)-1):
   for j in range(len(arr)-1-i):
    if arr[j] > arr[j+1]:
     arr[j], arr[j+1] = arr[j+1], arr[j]


while True:
    val = input()
    if val == "STOP":
        break
    else:
        arr = list(map(int, val.split()))
        diffLst = []
        for i in range(len(arr)-1):
            diffLst.append(abs(arr[i] - arr[i+1]))
        bubbleSort(diffLst)
        isUBJumper = True
        for i in range(len(diffLst)):
            if diffLst[i] != i+1:
                isUBJumper = False
                break
        if isUBJumper == True:
            ans.append('UB Jumper')
        else:
            ans.append('Not UB Jumper')
            
for i in ans:
    print(i)
        