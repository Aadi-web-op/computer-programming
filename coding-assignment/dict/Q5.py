#5 Find the intersection of two dictionaries
st = ({"a": 1, "b": 2, "c": 3},{"b": 2, "c": 4, "d": 3})
dc1 = (st[0])
dc2 = (st[1])
dc_inter = {}
for i in dc1:
    for j in dc2:
        if(j==i and dc2[j]==dc1[i]):
            dc_inter[i] = dc1[i]
print(dc_inter)