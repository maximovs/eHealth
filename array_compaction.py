def array_compact(input):
    last = None
    result = []
    for value in input:
        if last is None or last < value:
            last = value
            result.append(last)
        elif last > value:
            raise ValueError("Array should be sorted")
    return result

array = [1,2,2,2,3,4,4,4,5,6,7,8,8,8]
print array_compact(array)