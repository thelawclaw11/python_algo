import mathHelp


def bucket_sort(array, k):
    buckets = [[] for x in range(k)]
    print(buckets)
    M = max(array)

    for i in range(len(array)):
        buckets[math.floor(k * array[i] / M)].append(array[i])

    result = []

    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)
    return result


print(bucket_sort([9, 8, 7, 6, 5, 4, 3, 2, 1], 3))
