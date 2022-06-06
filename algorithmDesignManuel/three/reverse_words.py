def reverse(array, l, r):
    while l <= r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1

def reverse_words(s):
    array = list(s)

    reverse(array, 0, len(array) - 1)
    l = 0

    for r in range(len(array)):
        if array[r] == " ":
            reverse(array, l, r - 1)
            l = r + 1

    reverse(array, l, len(array) - 1)

    alpha = "".join(array)

    return alpha

print(reverse_words("My name is Chris"))


