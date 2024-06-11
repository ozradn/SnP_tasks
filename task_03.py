def max_odd(array):
    result = None
    for i in array:
        if isinstance(i, (int, float)) and i%2 != 0 and (result == None or result < i):
            result = i
    return result
