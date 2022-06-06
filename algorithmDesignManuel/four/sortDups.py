from collections import Counter


def sort_with_dups(arr):
    table = Counter(arr)
    uniqs = list(table.keys())
    uniqs.sort()

    result = []

    for n in uniqs:
        result.extend([n] * table[n])

    return result













print(sort_with_dups([2,2,2,3,3,1,1,1]))
