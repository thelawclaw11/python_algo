def cover_interval(intervals, interval_to_cover):
    intervals.sort()
    result = [[0,1]]

    i = 1

    while i < len(intervals):
        start, end = intervals[i]
        top_start, top_end = result[-1]

        if start > top_end:
            result.append(intervals[i - 1].copy())
            i -= 1

        if i == len(intervals) - 1:
            result.append(intervals[i].copy())
        i += 1

    return result


print(cover_interval([[1,1], [1,3], [2,3], [2,4], [2,10]], [1, 10]))
# print(cover_interval([[1,4], [4,8], [7,10]]))