
def partition(array, left, right, pivot):
    while left <= right:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left

def quickSort(array, left=0, right=None):
    right = len(array) - 1 if right is None else right

    if left >= right:
        return

    pivot = array[(left + right)//2]
    p = partition(array, left, right, pivot)

    quickSort(array, left, p - 1)
    quickSort(array, p, right)

    return None


alpha = [5, 8, 3, 2, 9, 10, 1, 4, 7, 6]

quickSort(alpha)

print(alpha)
