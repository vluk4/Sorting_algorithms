def shellSort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:

        for i in range(gap, size):
            j = i
            aux = arr[i]
            while j >= gap and arr[j - gap] > aux:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = aux
        gap = gap // 2
    return arr


list = [21, 651, 16, 1, 61, 16, 519, 1, 84, 984, 9, 10, 2, 9, 84, 1]
print(shellSort(list))