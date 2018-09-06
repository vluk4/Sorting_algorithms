def coutingSort(array):
    j = 0
    n = len(array)
    k = max(array) + 1
    aux = [0] * k
    sorted_array = [0] * n

    for i in range(n):
        aux[array[i]] += 1

    for i in range(k):
        tmp = aux[i]

        while tmp > 0:
            sorted_array[j] = i
            j += 1
            tmp -= 1
    return sorted_array


lista = [51, 561, 6, 16, 16, 51, 65156, 1, 684, 64, 894, 1, 31, 16, 49, 4]
print(coutingSort(lista))
