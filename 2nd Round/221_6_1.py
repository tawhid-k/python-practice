my_file = open('input1.txt', 'r')
output_file = open('output1.txt', 'w')

for file in my_file:
    arr = [-1] * 1000
    N = int(file)
    def dp(n):
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
    val = dp(N)
    output_file.write(str(val))
    
    