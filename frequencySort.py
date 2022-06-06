from collections import Counter

def compare(a,b):
    a_num, a_count = a
    b_num, b_count = b
    if a_count > b_count:
        return 1
    if b_count > a_count:
        return -1

class Solution:
    def frequencySort(self, nums):
        count = Counter(nums)

        alpha = list(count)
        alpha.sort(compare)
        return alpha



solution = Solution()
print(solution.frequencySort([1,1,2,2,2,3]))