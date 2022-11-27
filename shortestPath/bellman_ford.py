import math


def bellman_ford(graph, start):
    dist = {n: math.inf for n in graph.keys()}
    dist[start] = 0

    # set up distances as if there were no negative cycles
    for _ in range(len(graph)):
        for start, edges in graph.items():
            for end, weight in edges:
                dist[end] = min(dist[end], dist[start] + weight)

    #detect negative cycles
    for _ in range(len(graph)):
        for start, edges in graph.items():
            for end, weight in edges:
                new_dist = min(dist[end], dist[start] + weight)
                if new_dist < dist[end]:
                    dist[end] = -math.inf
    return dist


g = {
    "0": [("1", 5)],
    "1": [("6", 60), ("2", 20), ("5", 30)],
    "2": [("3", 10), ("4", 75)],
    "3": [("2", -15)],
    "4": [("9", 100)],
    "5": [("6", 5), ("8", 50), ("4", 25)],
    "6": [("7", -50)],
    "7": [("8", -10)],
    "8": [],
    "9": []
}

print(bellman_ford(g, "0"))
