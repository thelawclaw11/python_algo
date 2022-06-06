import heapq
import json
import os
import random
import uuid
from collections import namedtuple

PAGE_SIZE = 4

def prep():
    data = [[10, 19, 4, 2], [12, 5, 24, 14], [1, 4, 8, 25], [27, 29, 13, 29], [21, 23, 5, 4], [5, 8, 8, 25], [19, 3, 25, 3], [0, 25, 3, 29]]

    for i, page in enumerate(data):
        with open(f"page{i}.json", "w+") as f:
            json.dump(page, f)

def initializeRun(page_name):
    with open(page_name) as f:
        array = json.load(f)

    f.close()

    array.sort()

    with open(page_name, "w") as f:
        json.dump(array, f)

    f.close()

    smallest = min(array)
    return smallest, 1, [page_name]


def merge(left_run, right_run):
    left_smallest, left_length, left_file_names = left_run
    right_smallest, right_length, right_file_names = right_run

    merged_smallest = min(left_smallest, right_smallest)

    merged_file_names = []

    left_file_index = 0
    right_file_index = 0


    current_left_contents = json.load(open(left_file_names[left_file_index]))
    current_right_contents = json.load(open(right_file_names[right_file_index]))

    current_merge_contents = []

    l = 0
    r = 0

    while left_file_index < len(left_file_names) or right_file_index < len(right_file_names):
        if left_file_index < len(left_file_names) and right_file_index < len(right_file_names):
            if current_left_contents[l] < current_right_contents[r]:
                current_merge_contents.append(current_left_contents[l])
                l += 1
            else:
                current_merge_contents.append(current_right_contents[r])
                r += 1

        elif left_file_index < len(left_file_names):
            current_merge_contents.append(current_left_contents[l])
            l += 1

        elif right_file_index < len(right_file_names):
            current_merge_contents.append(current_right_contents[r])
            r += 1

        if l >= len(current_left_contents):
            l = 0
            left_file_index += 1
            if left_file_index < len(left_file_names):
                current_left_contents = json.load(open(left_file_names[left_file_index]))

        if r >= len(current_right_contents):
            r = 0
            right_file_index += 1
            if right_file_index < len(right_file_names):
                current_right_contents = json.load(open(right_file_names[right_file_index]))

        if len(current_merge_contents) == PAGE_SIZE:
            file_name = uuid.uuid4().hex
            json.dump(current_merge_contents, open(file_name, "w+"))
            merged_file_names.append(file_name)
            current_merge_contents = []

    for file_name in left_file_names + right_file_names:
        os.remove(file_name)

    return merged_smallest, len(merged_file_names), merged_file_names

# initializeRun('./page7.json')
# initializeRun('./page2.json')
# run = merge((0, 1, ['./page7.json']), (1,1, ['./page2.json']))

def sort(file_names):
    heap = []

    for name in file_names:
        run = initializeRun(name)
        heapq.heappush(heap, run)

    while len(heap) > 1:
        left_run = heapq.heappop(heap)
        right_run = heapq.heappop(heap)
        merged_run = merge(left_run, right_run)
        heapq.heappush(heap, merged_run)

    return heap[0][2]

prep()

new_file_names = sort(['./page0.json', './page1.json', './page2.json', './page3.json', './page4.json', './page5.json', './page6.json', './page7.json'])

def create_new_file(file_names):
    f = open("output.txt", "w+", encoding="utf-8")

    for file_name in file_names:
        numbers = json.load(open(file_name))
        for n in numbers:
            f.write(str(n))
            f.write(",")
        os.remove(file_name)

    f.close()
create_new_file(new_file_names)

