def reverse(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr) - 1) // 2

    left_half = reverse(arr[:mid + 1])
    right_half = reverse(arr[mid + 1:])

    return right_half + left_half



print(reverse([1,2,3,4,5,6,7,8, 9]))
# print(reverse([1,2,3,4,5,6,7,8]))
# print(reverse([1,2,3,4,5,6,7,8]))
