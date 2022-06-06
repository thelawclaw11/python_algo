def find_median():
    pass


def partition(array, left, right):
    pivot = array[right]

    i = left

    for j in range(left, right):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1

    array[right], array[i] = array[i], array[right]
    return i

def quickselect(array, k):
    target_index = len(array) - k

    def helper(left, right):

        p = partition(array, left, right)

        if p == target_index:
            return array[p]

        if p < target_index:
            return helper(p + 1, right)
        else:
            return helper(left, p - 1)

    return helper(0, len(array) - 1)

def find_median(array):
    return quickselect(array, (len(array) // 2) + 1)

def quicksort(array):
    def helper(left, right):
        if left >= right:
            return

        mid = partition(array, left, right)
        helper(left, mid - 1)
        helper(mid, right)

    helper(0, len(array) - 1)


a = [0, 3, 5, 1, 10, 7, 6, 2, 4, 9, 8]


print(find_median(a))


# partition(a, 0, len(a) - 1)

print(a)


