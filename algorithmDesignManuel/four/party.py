import bisect
from collections import defaultdict


def party(intervals):
    intervals.sort(key=lambda interval: interval[0])

    arrive, leave = [list(thing) for thing in zip(*intervals)]

    best = 0
    best_time = None

    for i in range(len(arrive)):
        index = bisect.bisect_left(arrive, leave[i], lo=i)

        people = index - i + 1 if index < len(arrive) and  arrive[index] <= leave[i] else index - i
        if people > best:
            best = people
            best_time = arrive[index] if index < len(arrive) else arrive[index - 1]

    return best_time

input = [
    [1,3],
    [5,7],
    [6,40],
    [10,20],
    [12,22],
    [13, 14]
]

print(party(input))
