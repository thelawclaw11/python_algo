class PQ:
    def __init__(self, xs=None):
        if xs is None:
            xs = []
        self.heap = [None] + xs

        for i in range(len(xs) // 2, 0, -1):
            self.bubble_down(i)

    def __len__(self):
        return len(self.heap) - 1

    def parent(self, n):
        if n == 1:
            return None

        return n // 2

    def child(self, n):
        return n * 2

    def bubble_up(self, n):
        if self.parent(n) is None:
            return

        if self.heap[n] < self.heap[self.parent(n)]:
            self.heap[n], self.heap[self.parent(n)] = self.heap[self.parent(n)], self.heap[n]
            self.bubble_up(self.parent(n))

    def insert(self, x):
        self.heap.append(x)
        self.bubble_up(len(self.heap) - 1)

    def get_min(self):
        if len(self.heap) == 1:
            return None

        if len(self.heap) == 2:
            return self.heap.pop()

        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.bubble_down(1)
        return result

    def bubble_down(self, n):
        min_index = n
        left_child = self.child(n)

        for c in range(left_child, left_child + 2):
            if c < len(self.heap):
                if self.heap[c] < self.heap[min_index]:
                    min_index = c

        if min_index != n:
            self.heap[n], self.heap[min_index] = self.heap[min_index], self.heap[n]
            self.bubble_down(min_index)


def heapSort(array):
    heap = PQ(array)
    result = []

    while heap:
        result.append(heap.get_min())

    return result


print(heapSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
