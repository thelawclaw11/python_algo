class MyHashSet:
    def __init__(self):
        self.array = [None] * 1000

    def do_hash(self, key: int) -> int:
        return key % len(self.array)

    def add(self, key: int) -> None:
        hash_value = self.do_hash(key)

        if self.array[hash_value] == None:
            self.array[hash_value] = [key]
        else:
            if not key in self.array[hash_value]:
                self.array[hash_value].append(key)

    def remove(self, key: int) -> None:
        hash_value = self.do_hash(key)

        if self.array[hash_value]:
            if key in self.array[hash_value]:
                self.array[hash_value].remove(key)
            if len(self.array[hash_value]) == 0:
                self.array[hash_value] = None

        return None

    def contains(self, key: int) -> bool:
        hash_value = self.do_hash(key)

        if self.array[hash_value] == None:
            return False
        else:
            return key in self.array[hash_value]


my_set = MyHashSet()

val = 1000000

my_set.add(val)

print(my_set.array)

print(my_set.contains(val))