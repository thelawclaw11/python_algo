import collections


def seat_wedding_guests(graph):
    A = set()
    B = set()

    def bfs(start):
        q = collections.deque([start])

        current = A

        while q:
            n = len(q)
            for _ in range(n):
                node = q.pop()

                if any([enemy in current for enemy in graph[node]]):
                    return False

                current.add(node)

                for enemy in graph[node]:
                    if enemy not in A and enemy not in B:
                        q.appendleft(enemy)

            current = A if current == B else B

        return True

    for k, enemies in enumerate(graph):
        if k in A or k in B:
            continue

        if not bfs(k):
            return False, set(), set()

    return True, A, B


print(seat_wedding_guests(
[[1,3],[0,2],[1,3],[0,2]]
))