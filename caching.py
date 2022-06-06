from functools import lru_cache
from typing import List


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(100))

def square_root(n: int) -> int:
    def search(left, right):

        mid = (left + right) // 2

        square_of_next = (mid + 1) * (mid + 1)
        square_of_current = mid * mid

        if square_of_current <= n and square_of_next > n:
            return mid

        if square_of_current > n:
            return search(left, mid - 1)

        if square_of_current < n:
            return search(mid + 1, right)

    return search(0, n)


def find_min_rotated(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        # if <= last element, then belongs to lower half
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index