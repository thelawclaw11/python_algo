#
#     def F(arr, left, right):
#         if left >= right:
#             return
#         pivot = arr[(left + right) // 2]
#         index = partition(arr, left, right, pivot)
#         F(arr, left, index - 1)
#         F(arr, index, right)
#
#     def partition(arr, left, right, pivot):
#         while left <= right:
#             while arr[left] < pivot:
#                 left += 1
#
#             while arr[right] > pivot:
#                 right -= 1
#
#             if left <= right:
#                 arr[left], arr[right] = arr[right], arr[left]
#                 left += 1
#                 right -= 1
#         return left
#
#     F(array, 0, len(array) - 1)
#
#
# array = [1,4,5,3,2]
#
#
# quickSort(array)
