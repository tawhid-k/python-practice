def binary(s):
    if s <= 0:
        return 0
    v = ""
    v = str(binary(int(s/2))) + str(s%2)
    return v

print(binary(456))