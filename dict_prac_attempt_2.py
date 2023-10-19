d1 = {'a':2, 'b':2}
d2 = {'c':99}
def dict_merge_sum(d1, d2):
    merged_dict = d1.copy()
    for key, value in d2.items():
        if key in d1:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict
print(dict_merge_sum(d1, d2))

