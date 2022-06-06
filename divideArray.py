import math


def divideArray(array, k):
    max_size = math.floor(len(array) / k)

    partitions = [[]]

    for n in enumerate(array):
        if len(partitions[-1]) == max_size:
            partitions.append([])

        if len(partitions[-1]) < max_size:
            partitions[-1].append(n)

    return partitions

print(divideArray([1,2,3,4,5,6,7,8,9,10],3))



# def divideArray(array, k):
#     max_size = math.ceil(len(array) / k)
#
#     partitions = [[]]
#
#     for i, n in enumerate(array):
#         if len(partitions[-1]) == max_size:
#             max_size = math.ceil((len(array) - i) / (k - len(partitions)))
#             partitions.append([])
#
#         if len(partitions[-1]) < max_size:
#             partitions[-1].append(n)
#
#     return partitions