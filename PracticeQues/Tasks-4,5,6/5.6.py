def flatten(lst):
    result = []
    for item in lst:

        if type(item) == list:
            result = result + flatten(item)
        else:
            result.append(item)
    return result
print(flatten([1, [2, 3, [4, [5, 6]], 7], 8]))
print(flatten([[[[1]]], 2, [[3, [4]]]]))