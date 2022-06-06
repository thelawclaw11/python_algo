class Solution:
    def validPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        used_deletion = False

        while L <= R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                if used_deletion:
                    return False
                elif s[L + 1] == s[R]:
                    L += 2
                    R -= 1
                    used_deletion = True
                elif s[L] == s[R - 1]:
                    L += 1
                    R -= 2
                    used_deletion = True
                else:
                    return False


        return True


solution = Solution()
print(solution.validPalindrome("aba"))
print(len("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))