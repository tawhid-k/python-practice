c = [[0 for i in range(100)] for j in range(100)]
t = [[None for i in range(100)] for j in range(100)]
def LCS(X, Y):
    m = len(X) 
    n = len(Y) 
    for i in range(m):
      for j in range (n):
        if X[i] == Y[j]:
           c[i][j] = c[i-1][j-1]+1
           #t[i,j]<- diagonal
        elif c[i-1][j] >= c[i][j-1]:
           c[i][j] = c[i-1][j]
           #t[i][j] <- up
        else:
           c[i][j] = c[i][j-1]
           #t[i,j] <- left
         
X = 'YRSPFMHI'
Y = 'YPSRFMHI'
LCS(X, Y)

print(c[len(X)-1][len(Y)-1])
