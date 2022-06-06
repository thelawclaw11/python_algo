import heapq
import time
import timeit

read_start = time.time()
raw_text = ""
with open("war_and_peace.txt") as f:
    raw_text = f.read()



text = raw_text.replace("\n", "")

raw_words = text.split(" ")

words = [word for word in raw_words if word != ""]

read_end = time.time()

print(read_end - read_start)

def heapsort(array):
    heap = array
    heapq.heapify(heap)

    result = []

    while heap:
        result.append(heapq.heappop(heap))

    return result

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

start = time.time()
result = quickSort(words)
end = time.time()

print(end - start)
