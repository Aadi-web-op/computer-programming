# 7 Count the occurrences of each character in a string

dct = {}
st = input()
d = ''
for i in st:
    if i not in d:
        d += i
        count = st.count(i)
        dct[i] = count
print(dct)