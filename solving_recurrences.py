import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return F(n - 1) + 2 * F(n - 2)

# 349525
print(F(20))


def F2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n % 2 == 0:
        return 2 * F2(n - 1) - 1

    return 2 * F2(n - 1) + 1

print(F2(20))

def F3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return 2 * F3(n - 1) - ((-1) ** n)

print(F3(20))

def F4(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return ((1/3) * (2 ** n)) - ((1/3) * (-1) ** n)

print(F4(20))

assert F(20) == F2(20) == F3(20) == int(F4(20))