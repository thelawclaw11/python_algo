from typing import List


def get_prime_factors(n):
    result = []

    k = 2
    remainder = n
    while k <= remainder:
        if remainder % k == 0:
            result.append(k)
            remainder //= k
        else:
            k += 1

    if n in result:
        result.remove(n)

    return result


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        prime_factors = get_prime_factors(n)

        result = []
        accum = []

        def F(remainder, start):
            if remainder == 1:
                result.append(accum[:])
                return

            for i in range(start, len(prime_factors)):
                accum.append(prime_factors[i])
                F(remainder // prime_factors[i], i + 1)
                accum.pop()

        F(n, 0)
        return result

solution = Solution()

print(solution.getFactors(60))
# print(solution.getFactors(10000001))
