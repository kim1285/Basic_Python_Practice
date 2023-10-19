d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':2, 'b':2, 'd':3, 'e':2}
def dict_merge_sum(d1, d2):
    from copy import deepcopy
    d3 = deepcopy(d1)
    d1.update(d2)
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for value in d1.values():
        l1.append(value)
    for value in d3.values():
        l2.append(value)
    for i in range(len(l1)):
        try:
            l3.append(l1[i] + l2[i])
        except IndexError:
            try:
                l3.append(l1[i])
            except IndexError:
                pass
            try:
                l3.append(l2[i])
            except IndexError:
                pass
    for key in d1.keys():
        l4.append(key)
    d4 = dict(zip(l4, l3))
    return print(d4)

dict_merge_sum(d1, d2)