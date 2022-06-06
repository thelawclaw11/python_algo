import random
import unittest


def merge(left, right):
    result = []

    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    while l < len(left):
        result.append(left[l])
        l += 1

    while r < len(right):
        result.append(right[r])
        r += 1

    return result


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)




print(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

print([random.randint(0,1000) for _ in range(10)])

# [70, 97, 99, 333, 480, 577, 765, 767, 768, 917]
# 5

[1,6,13,19,20]
4