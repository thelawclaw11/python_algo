from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        GT = "GT"
        LT = "LT"
        EQ = "EQ"

        relations = []

        for k in range(len(arr) - 1):
            if arr[k] == arr[k + 1]:
                relations.append(EQ)
            elif arr[k] > arr[k + 1]:
                relations.append(GT)
            else:
                relations.append(LT)

        relations.append(None)

        result = 1

        left = 0
        while relations[left] == EQ:
            left += 1

        for right in range(left,len(relations)):
            result = max(result, right - left + 1)

            if right == left:
                continue

            if relations[right] == EQ:
                left = right + 1
            elif relations[right] == relations[right - 1]:
                left = right
        return result

solution = Solution()
# 1
print(solution.maxTurbulenceSize([9,9,9,9,9,9]))

# 5
# print(solution.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))

# 2
# print(solution.maxTurbulenceSize([4, 8, 12, 16]))

# 6
# print(solution.maxTurbulenceSize([2,2,0,2,4,2,5,0,1,2,3]))

# for left in range(len(relations)):
#     if relations[left] == EQ:
#         continue
#     for right in range(left + 1, len(relations)):
#         result = max(result, right - left + 1)
#
#         if relations[right] == relations[right - 1] or relations[right] == EQ:
#             break