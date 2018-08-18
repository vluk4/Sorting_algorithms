def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def mergeSort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return merge(mergeSort(left), mergeSort(right))


number_array = [5, 8, 9, 4, 8, 6, 8, 7, 89, 4, 1, 5, 7, 7, 8, 4, 1, 8]
print(mergeSort(number_array))
