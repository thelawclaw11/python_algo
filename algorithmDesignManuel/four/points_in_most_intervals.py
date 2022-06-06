import bisect
import math


def points_in_most_intervals(intervals):
    points_of_interest = set()

    for start, end in intervals:
        points_of_interest.add(start)
        points_of_interest.add(end)

    l = list(points_of_interest)
    l.sort()
    l.append(math.inf)

    table = {n: 0 for n in l}

    for start, end in intervals:
        table[start] += 1

        index = bisect.bisect_left(l, end)
        table[l[index + 1]] -= 1

    best = 0
    best_element = None

    current = 0

    for n in l:
        current += table[n]

        if current >= best:
            best = current
            best_element = n

    return best_element











print(points_in_most_intervals([
    [10,40],
    [15,70],
    [20,60],
    [50,90]
]))
