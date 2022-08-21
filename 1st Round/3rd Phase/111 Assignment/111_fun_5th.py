def isPalindrome(s):
    s = s.replace(' ', '')
    l = len(s)
    j = l-1
    for i in range(int(l/2)):
        if s[i] != s[j]:
            return False
        j -= 1
    return True

if isPalindrome('madam'):
    print('Palindrome')
else:
    print('Not a palindrome')
    
if isPalindrome('hello'):
    print('Palindrome')
else:
    print('Not a palindrome')
    
if isPalindrome('nurses run'):
    print('Palindrome')
else:
    print('Not a palindrome')
    