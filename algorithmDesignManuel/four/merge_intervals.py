def merge_intervals(intervals):
    intervals.sort(key=lambda interval: interval[0])

    result = [intervals[0]]

    for start, end in intervals[1:]:
        top_start, top_end = result[-1]

        if start <= top_end:
            # extends previous interval
            result[-1][1] = max(end, top_end)
        elif start > top_end:
            # intervals are disjoint
            result.append([start, end])

    return result


print(merge_intervals([[1, 3], [2, 6], [8, 10], [7, 18]]))
