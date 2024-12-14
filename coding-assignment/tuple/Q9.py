# Write a Python program to find the repeated items of a tuple. 

tup = ('1','2','3','3','3','4','5','6','6','8','9','9')
dc = ''
for i in tup:
    if i not in dc:
        if tup.count(i) > 1:
            dc += i
for i in dc:
    print(i)