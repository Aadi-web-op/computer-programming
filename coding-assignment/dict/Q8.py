# 8 Remove keys with None values from a dictionary

dct = eval(input())
dt = {}
for i in dct:
    value = dct[i]
    if dct[i] != None:
        dt[i] = value
print(dt)