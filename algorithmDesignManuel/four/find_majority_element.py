from collections import Counter


def find_majority_element(array):
    counts = Counter(array)

    for num, count in counts.items():
        if count > len(array) // 2:
            return num

    return None

def find(array):
    counts = Counter(array)

    result = []

    for num, count in counts.items():
        if count >= len(array) / 4:
            result.append(num)

    return result


print(find([1,1,1,2,2,2,3,3,3,4,4,4]))

