from collections import deque
from typing import List


def hash(key, table_size):
    return key % table_size


class MyHashMap:

    def __init__(self):
        self.table = [None] * 100

    def put(self, key: int, value: int) -> None:
        hashed_key = hash(key, len(self.table))
        pair = (key, value)
        if self.table[hashed_key]:
            self.table[hashed_key].append(pair)
        else:
            self.table[hashed_key] = deque()
            self.table[hashed_key].append(pair)



    def get(self, key: int) -> int:
        hashed_key = hash(key, len(self.table))

        if self.table[hashed_key] is not None:
            for current_key, current_value in self.table[hashed_key]:
                if current_key == key:
                    return current_value
        return -1


    def remove(self, key: int) -> None:
        hashed_key = hash(key, len(self.table))
        if len(self.table[hashed_key]) == 1:
            self.table[hashed_key] = None
        else:
            for index, (current_key, current_value) in enumerate(self.table[hashed_key]):
                if current_key == key:
                    del self.table[hashed_key][index]
                break


hashMap = MyHashMap()
print(hashMap.put(1,1))
print(hashMap.put(2,2))
print(hashMap.get(1))
print(hashMap.get(3))
print(hashMap.put(2,1))
print(hashMap.get(2))
print(hashMap.remove(2))
print(hashMap.get(2))
