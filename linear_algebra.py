

def add(left, right):
    if len(left) != len(right):
        raise Exception("Can only add vectors of the same length")

    return [l + r for l, r in zip(left, right)]


def scale(vector, scalar):
    return [x * scalar for x in vector]

a = [1,2,3]
b = [3,4,5]

print(add(a, b))



