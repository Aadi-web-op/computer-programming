# write a program to count frequency of elements in list and return in the form of a dictionary.

ls = eval(input())
dct = {}
for i in ls:
    count = ls.count(i)
    dct[i] = count
print(dct)