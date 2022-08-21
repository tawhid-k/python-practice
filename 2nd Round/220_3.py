def hocBuilder(height):
    if height - 5 >= 8:
        return 1 + hocBuilder(height - 5)
    elif height - 5 >= 3:
        return 1
    else:
        return 0
    
print(hocBuilder(8))
print(hocBuilder(5))
print(hocBuilder(20))
            