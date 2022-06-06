def get_subsets(arr):

    result = []

    accum = []
    def F(start):
        result.append(accum[:])

        if len(accum) == len(arr):
            return

        for i in range(start, len(arr)):
            accum.append(arr[i])
            F(i + 1)
            accum.pop()






print(get_subsets([1,2,3]))

def get_subsets(arr):

    result = []

    accum = []
    def F(start):

        if start == len(arr):
            result.append(accum.copy())
            return

        accum.append(arr[start])
        F(start + 1)
        accum.pop()
        F(start + 1)


    F(0)
    return result
