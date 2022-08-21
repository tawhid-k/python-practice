def capital(s):
    news = ""
    news += s[0].upper()
    for i in range(1, len(s), 1):
        if s[i-1] == '.' or s[i-1] == '!' or s[i-1] == '?':
            news += s[i].upper()
        elif s[i] == 'i' and s[i+1] == ' ':
            news += 'I'
        else:
            news += s[i]
    return news
    
s = 'my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much.'
print(capital(s))