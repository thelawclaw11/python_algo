import math


class SparseTable:
    def __init__(self, array):
        rows = math.floor(math.log2(len(array)))
        self.table = [[None] * len(array) for _ in range((rows + 1))]
        self.table[0] = array

        for row in range(1, len(self.table)):
            for col in range(len(array)):
                start = self.table[row - 1][col]
                end_col = col + (2 ** (row - 1))

                if end_col >= len(array) or self.table[row - 1][end_col] is None:
                    break

                end = self.table[row - 1][end_col]
                self.table[row][col] = min(start, end)

    def get_range_min(self, l, r):
        length = r - l + 1
        row = math.floor(math.log2(length))
        k = 2 ** row
        return min(self.table[row][l], self.table[row][r - k + 1])


st = SparseTable([4, 2, 3, 7, 1, 5, 3, 3, 9, 6, 7, -1, 4])
print(st.get_range_min(8, 12))

# for row in st.table:
#     print(row)
