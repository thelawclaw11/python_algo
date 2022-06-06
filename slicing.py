import random


def is_palindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True


alpha = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(alpha[-3:])

# print(alpha[:-2], alpha[-2:])
#
# print([random.randint(1,10) for _ in range(5)])
