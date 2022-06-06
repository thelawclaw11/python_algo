import random
from heapq import heappush, heappop


def find_second_largest(array):
    heap = []

    for n in array:
        heappush(heap, n)
        if len(heap) > 2:
            heappop(heap)

    return min(heap)

def find_third_largest(array):
    heap = []

    for n in array:
        heappush(heap, n)
        if len(heap) > 3:
            heappop(heap)

    return min(heap)








array = [6, 5, 1, 7, 3, 9, 4, 2, 10, 8]

print(find_second_largest(array))
print(find_third_largest(array))

# random.shuffle(array)
# print(array)