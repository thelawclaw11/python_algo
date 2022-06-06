from collections import defaultdict, Counter


def is_anagram(left, right):
    left_table = Counter(left)
    right_table = Counter(right)
    return left_table == right_table

print(is_anagram("incest", "insect"))
print(is_anagram("patio", "piano"))