class Solution:
    def maximalRectangle(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        best = 0

        # for row in range(0, rows):
        #     for col in range(0, cols):



solution = Solution()
alpha = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(solution.maximalRectangle(alpha))
