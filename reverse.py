def reverse(array):
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    return array


print(reverse([1,2,3,4,5]))
print(reverse([1,2,3,4]))

print("Canon"[::-1])