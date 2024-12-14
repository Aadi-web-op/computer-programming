# 3 Invert a dictionary (keys become values and values become keys)

def invert_dict(d):
    {v:k for k,v in d.items()}
print(invert_dict({"a": 1, "b": 2, "c": 3}))