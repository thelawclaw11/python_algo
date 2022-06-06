def get_h_index(papers):
    papers.sort()

    for i, count in enumerate(papers):
        num_greater_than = len(papers) - i

        if num_greater_than < count:
            return num_greater_than

papers = [50, 40, 33, 23, 12, 11, 8, 5, 1, 0]

print(get_h_index(papers))