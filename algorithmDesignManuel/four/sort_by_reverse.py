def reverse(array, left, right):
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


# a = [2, 9, 7, 3, 5, 10, 6, 4, 8, 1]
# sort_by_reverse(a)
# print(a)

b = [1,2,3,4,5]
reverse(b, 0, 4)
print(b)