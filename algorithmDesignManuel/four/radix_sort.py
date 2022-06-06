def get_kth_least_significant_digit(num, k):
    a = 10 ** k
    b = a // 10

    return (num % a) // b

def radix_sort(array):
    buckets = [[] for _ in range(10)]

    max_num = max(array)

    k = 1

    while (10 ** k) < (max_num ** 10):
        for n in array:
            digit = get_kth_least_significant_digit(n, k)
            buckets[digit].append(n)

        array = []
        for bucket in buckets:
            for n in bucket:
                array.append(n)

        buckets = [[] for _ in range(10)]

        k += 1

    return array



print(radix_sort([5832, 321, 97, 89, 3, 9111]))






def counting_sort(array):
    max_key = max(array)

    table = [0] * (max_key + 1)

    for n in array:
        table[n] += 1

    result = []

    for n, count in enumerate(table):
        result.extend([n] * count)

    return result