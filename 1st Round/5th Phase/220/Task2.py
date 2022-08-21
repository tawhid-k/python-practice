#220 Task2

vowel = 'AEIOU'

hashTable = [None] * 9

def hashCode(s):
    consonants = 0
    sumOfDigits = 0
    for i in s:
        if i >= 'A' and i <= 'Z' and i not in vowel:
            consonants += 1
        elif i >= '0' and i <= '9':
            sumOfDigits += int(i)
    code = (consonants * 24 + sumOfDigits) % 9
    return code
    
def insertHashValue(s):
    code = hashCode(s)
    if hashTable[code] == None:
        hashTable[code] = s
    else:
        for i in range(9):
            idx = (code + i) % 9
            if hashTable[idx] == None:
                hashTable[idx] = s
                break

s1 = "AKJ1OPWE"
s2 = "BILO2DF8"
s3 = "C23A2G98"

insertHashValue(s1)
insertHashValue(s2)
insertHashValue(s3)

print(hashTable)    