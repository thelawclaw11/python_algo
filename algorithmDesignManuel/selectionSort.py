from functools import lru_cache
@lru_cache(maxsize=None)
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

alpha = [6,3,5,7,1,2,9,10,8,4]

selection_sort(alpha)

print(alpha)