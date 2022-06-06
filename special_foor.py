# import math
#
# from sortedcontainers import SortedList
#
#
# class CountIntervals:
#
#     def __init__(self):
#         self.count = 0
#         self.intervals = SortedList()
#
#     def add(self, left: int, right: int) -> None:
#         if len(self.intervals) == 0:
#             self.intervals.add((left, right))
#
#         start_index = self.intervals.bisect_left((left, right))
#         end_index = self.inverals.bisect_right((right, math.inf))
#
#         end_interval_start, end_interval_end = self.intervals[end_index]
#
#
#
#
#
#         print(start_index)
#         end_index
#
#         for i in range(start_index, )
#
#     def count(self) -> int:
#         return self.count
#
#
# countIntervals = CountIntervals()
#
# countIntervals.add(2,3)

