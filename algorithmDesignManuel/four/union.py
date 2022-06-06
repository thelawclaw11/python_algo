def union(A, B):
    A.sort()
    B.sort()

    result = []

    a = 0
    b = 0

    while a < len(A) and b < len(B):
        if A[a] == B[b]:
            result.append(A[a])
            a += 1
            b += 1
        elif A[a] < B[b]:
            a += 1
        elif B[b] < A[a]:
            b += 1
    return result

def union(A, B):
    A_set = set(A)

    result = []

    for b in B:
        if b in A_set:
            result.append(b)
    return result




print(union([1,2,3,7,8], [2,3,8]))