def sort(arr):

    i = 0

    for n in [1, 2]:
        for j in range(i, len(arr)):
            if arr[j] == n:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

a = [2, 3, 1, 1, 1, 2, 3, 3, 2, 1, 2, 2, 3, 2, 2, 1]

sort(a)

print(a)
