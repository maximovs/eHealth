# I asume it should be rotated in place.
def rotate_array(array, n):
    size = len(array)
    queue = list()
    if n > size:
        raise ValueError("n cant be bigger than the array")
    for i in range(0, n):
        queue.append(array[i])
    for i in range(n, size + n):
        index = i % size
        if i < size:
            queue.append(array[index])
        array[index] = queue.pop(0)

array = [1, 2, 3, 4, 5, 6]
rotate_array(array, 2)
print array