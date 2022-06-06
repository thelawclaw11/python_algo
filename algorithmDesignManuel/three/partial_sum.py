class PartialSum:

    def __init__(self, array):
        self.partial_sum_array = []

        for n in array:
            prev = self.partial_sum_array[-1] if self.partial_sum_array else 0
            self.partial_sum_array.append(prev + n)
        print(self.partial_sum_array)


    def add(self, index, value):
        for i in range(index, len(self.partial_sum_array)):
            self.partial_sum_array[i] += value

    def get_partial_sum(self, end):
        return self.partial_sum_array[end]
