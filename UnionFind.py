class UnionFind:
    def __init__(self):
        self.f = {}

    def find(self, x):
        y = self.f.get(x, x)
        if y != x:
            y = self.find(y)
        return y

    def union(self, x, y):
        self.f[self.find(x)] = self.find(y)


uf = UnionFind()

uf.union("a", "b")
uf.union("a", "c")
print(uf.find("a"))
print(uf.f)
