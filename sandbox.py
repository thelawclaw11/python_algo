from bisect import bisect_left, bisect_right

alpha = [1, 2, 4, 4, 7, 8, 9]
beta = [3, 4, 4, 4, 5, 6, 10]

def get_gt(array, x):
    left = bisect_right(array, x)
    return len(array) - left

def get_lt(array, x):
    right = bisect_left(array, x)
    return right

def get_count(array, x):
    left = bisect_left(array, x)
    right = bisect_right(array, x)
    return right - left


print(get_count(beta, 4))

# print(get_lt(beta, 4))
# print(get_lt(beta, 0))
# print(get_lt(beta, 0))

# print(get_gt(beta, 4))
# print(get_gt(beta, 2))
# print(get_gt(beta, 7))
# print(get_gt(beta, 6))
# print(get_gt(beta, 5))

# print(len(beta) - bisect_left(beta, 4))