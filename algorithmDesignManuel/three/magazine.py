from collections import defaultdict


def check(text, search):
    text_table = defaultdict(int)
    search_table = defaultdict(int)

    for c in search:
        search_table[c] += 1

    for c in text:
        text_table[c] += 1

    for char, count in search_table.items():
        if text_table[char] < count:
            return False

    return True



# True
print(check("canon is the best", "stanis"))
