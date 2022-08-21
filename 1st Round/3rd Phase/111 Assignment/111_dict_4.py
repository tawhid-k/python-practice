msg = dict()
msg[1] = '.,?!:'
msg[2] = 'ABC'
msg[3] = 'DEF'
msg[4] = 'GHI'
msg[5] = 'JKL'
msg[6] = 'MNO'
msg[7] = 'PQRS'
msg[8] = 'TUV'
msg[7] = 'WXYZ'
msg[0] = ' '

text = str.upper(input())

for i in text:
    for j in msg:
        if i in msg[j]:
            for k in range(msg[j].find(i)+1):
                print(j,end='')


