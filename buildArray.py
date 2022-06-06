class Solution:
    def buildArray(self, target, n):
        operations = []
        current_target_index = 0
        for num in range(1, n + 1):
            if current_target_index >= len(target):
                break
            if num == target[current_target_index]:
                operations.append("Push")
                current_target_index += 1
            else:
                operations.append("Push")
                operations.append("Pop")
        return operations


solution = Solution()

#print(solution.buildArray([1, 3], 3))
print(solution.buildArray([1,2], 4))
