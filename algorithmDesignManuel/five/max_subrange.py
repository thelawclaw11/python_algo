def max_subrange(array):
    def F(lo, hi):
        if lo == hi:
            return array[lo]

        mid = (lo + hi) // 2

        max_in_left = F(lo, mid)
        max_in_right = F(mid + 1, hi)

        best_left_sum = 0
        current_left_sum = 0
        l = mid

        while l >= lo:
            current_left_sum += array[l]
            best_left_sum = max(best_left_sum, current_left_sum)
            l -= 1

        best_right_sum = 0
        current_right_sum = 0
        r = mid + 1

        while r <= hi:
            current_right_sum += array[r]
            best_right_sum = max(best_right_sum, current_right_sum)
            r += 1

        max_crossing_sum = best_left_sum + best_right_sum

        return max(max_in_left, max_in_right, max_crossing_sum)

    return F(0, len(array) - 1)

def slow(array):

    result = 0
    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            result = max(result, current_sum)
    return result




print(max_subrange([-17, 5, 3, -10, 6, 1, 4, -3, 8, 1, -13, 4]))
print(slow([-17, 5, 3, -10, 6, 1, 4, -3, 8, 1, -13, 4]))