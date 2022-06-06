import random


def swap_negatives(array):
    i = 0

    for j in range(len(array)):
        if array[j] < 0:
            array[j], array[i] = array[i], array[j]
            i += 1

    return array




print(swap_negatives([2, 1, -3, 8, -9, 2, 4, -6, 10, -1, -2, -3, 4]))

a = [1,2,3,4,5,6,7,8,9,10]

random.shuffle(a)

print(a)

