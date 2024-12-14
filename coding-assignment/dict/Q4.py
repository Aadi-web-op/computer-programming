#4 Group elements of a list by their frequency
def list_by_freq(lst):
    dict = {}
    for i in lst:
        count = lst.count(i)
        dict[i] = count
    print(dict)

list_by_freq([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])