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
        gap = gap//2

