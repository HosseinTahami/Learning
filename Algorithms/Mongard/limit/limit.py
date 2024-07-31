"""
    [1, 2, 3, 4, 5]

        min 3 => [3, 4, 5]
        max 3 => [3, 4, 5]
        max, min 3 => [3]

""" 

def limit(array, min=None, max=None):
    min_check = lambda value: True if min is None else (value >= min)
    max_check = lambda value: True if max is None else (value <= max)

    return [value for value in array if min_check(value) and max_check(value)]

print(limit([1,2,3,4,5,6,7,8], 3, 7))
