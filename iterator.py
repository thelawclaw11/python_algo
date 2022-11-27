from dataclasses import dataclass


@dataclass
class Item:
    char: str
    count: int


class StringIterator:

    def __init__(self, cs: str):
        self.items = []

        i = 0

        while i < len(cs):
            c = cs[i]
            i += 1
            num_s = ""

            while i < len(cs) and cs[i].isdigit():
                num_s += cs[i]
                i += 1

            self.items.append(Item(c, int(num_s)))

        self.i = 0
        print(self.items)

    def next(self) -> str:
        if self.hasNext():
            current = self.items[self.i]
            if current.count > 0:
                current.count -= 1
            else:
                self.i += 1
                current = self.items[self.i]
                current.count -= 1
            return current.char

        return " "

    def hasNext(self) -> bool:
        current = self.items[self.i]

        if current.count > 0:
            return True

        if current.count == 0 and self.i == len(self.items) - 1:
            return False

        if self.i < len(self.items):
            return True

        return False

si = StringIterator("x6")

out = ""

out += si.next()
out += si.next()
out += si.next()
out += si.next()
out += si.next()
out += si.next()
out += si.next()
out += si.next()
