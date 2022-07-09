def get_prefixes(word):
    result = []

    for i in range(1,len(word) + 1):
        result.append(word[:i])

    return result



print(get_prefixes("apple"))

