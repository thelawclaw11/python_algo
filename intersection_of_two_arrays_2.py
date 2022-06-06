from collections import Counter
class Solution:
    def intersect(self, left, right):
        left_counter = Counter(left)
        right_counter = Counter(right)

        result = []

        for num, count in left_counter.items():
            num_to_add = min(count, right_counter[num])
            result.extend([num for i in range(num_to_add)])
        return result



# [2,2]
solution = Solution()
print(solution.intersect(left=[4, 9, 5], right=[9, 4, 9, 8, 4]))