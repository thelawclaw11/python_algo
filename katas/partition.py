def partition(arr, left, right):
    pivot_value = arr[right]

    i = left

    for j in range(left, right):
        if arr[j] < pivot_value:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quickselect(arr, k):
    target_index = len(arr) - k

    def helper(left, right):
        p = partition(arr, left, right)

        if target_index == p:
            return arr[p]

        if target_index > p:
            return helper(p + 1, right)

        if target_index < p:
            return helper(left, p - 1)



    return helper(0, len(arr) - 1)






def quicksort(arr):

    def helper(left, right):
        if left >= right:
            return

        p = partition(arr, left, right)
        helper(left, p - 1)
        helper(p, right)

    helper(0, len(arr) - 1)

    return arr







# alpha = [2]
# partition(alpha,0,0)
# print(alpha)

print(quickselect([7,2,1,8,6,3,5,4], 2))
# print(partition([7,2,1,8,3,5,4,6], 0, 7))
# print(partition([7,2,1,8,6,3,5,4,9], 0, 8))