def radixSort(array):
    base = 10

    def list_to_buckets(array, base, iteration):
        buckets = [[] for x in range(base)]
        for number in array:
            digit = (number // (base ** iteration)) % base
            buckets[digit].append(number)
        return buckets

    def buckets_to_list(buckets):
        numbers = []
        for bucket in buckets:
            for number in bucket:
                numbers.append(number)
        return numbers

    maxval = max(array)
    i = 0
    while base ** i <= maxval:
        array = buckets_to_list(list_to_buckets(array, base, i))
        i += 1
    return array

list = [5, 46, 49, 4, 984, 51, 65, 89, 4, 2, 1, 64]
print(radixSort(list))