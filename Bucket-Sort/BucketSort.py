def bucketSort(array):
    largest = max(array)
    length = len(array)
    size = largest / length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(array[i] / size)
        if j != length:
            buckets[j].append(array[i])
        else:
            buckets[length - 1].append(array[i])

    for i in range(length):
        buckets[i].sort()

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


list = [51, 54, 8, 48, 4, 4125, 84, 4, 2, 1, 216, 6, 6]
print(bucketSort(list))
