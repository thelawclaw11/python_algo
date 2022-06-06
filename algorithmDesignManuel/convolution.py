from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(top, bottom, left, right):
            if top > bottom or left > right:
                return False

            min_element = matrix[top][left]
            max_element = matrix[bottom][right]

            if min_element == target:
                return True

            if target < min_element or target > max_element:
                return False

            mid_row = (top + bottom) // 2
            mid_col = (left + right) // 2

            a = search(top, mid_row, left, mid_col)
            b = search(top, mid_row, mid_col + 1, right)
            c = search(mid_row + 1, bottom, left, mid_col)
            d = search(mid_row + 1, bottom, mid_col + 1, right)

            return a or b or c or d

        return search(0, len(matrix) - 1, 0, len(matrix[0]) - 1)


solution = Solution()

print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))