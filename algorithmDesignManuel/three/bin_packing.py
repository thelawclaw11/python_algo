import random
from sortedcontainers import SortedList

tree = SortedList([2, 4, 5, 6, 8, 9])

index = tree.bisect_right(1)


def best_fit(nums):
    tree = SortedList()

    for n in nums:
        target = 10 - n

        if not tree:
            tree.add(n)
        else:
            index = tree.bisect_left(target)
            if index > len(tree) - 1:
                tree.add(n)
                continue

            if tree[index] > target:
                index -= 1

            if index < 0:
                tree.add(n)
                continue

            updated_bin = tree[index] + n

            del tree[index]

            tree.add(updated_bin)

    print(tree)

    return len(tree)

def worst_fit(nums):
    tree = SortedList()

    for n in nums:
        if not tree:
            tree.add(n)
            continue
        maxi = 10 - n

        smallest = tree[0]

        if smallest > maxi:
            tree.add(n)
        else:
            del tree[0]
            tree.add(smallest + n)
    print(tree)

    return len(tree)

print(worst_fit([2, 1, 6, 6, 5, 10, 6, 6, 5, 2]))



# array = [3, 1, 7, 3, 8, 3, 3, 9, 10, 8]

# for _ in range(1000):
#     array = []
#     for _ in range(10):
#         array.append(random.randint(1,10))
#
#     print(array)
#     assert best_fit(array) == best_fit2(array)

print(best_fit([2, 1, 6, 6, 5, 10, 6, 6, 5, 2]))

# a = [8, 6, 8, 7, 8, 3]
#
# print(best_fit(a))
# print(best_fit2(a))


# print(best_fit([500, 300, 800, 1000, 100, 600, 200, 100]))
