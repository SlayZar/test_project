# unformatted code
from collections import deque

f = {
    "oooooooooooooooooooooooooooooooooooo": 123,
    "ldflgkgkdotigksdsvmdlgvksmvlkgvm": 43565865866568586895968565968958968758634,
}
graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "csdadaedseda": ["e"],
    "ddaedadadedaed": ["f"],
    "edadaedadaedeada": [],
    "fdaeddadadadaededadadaededeeeeeeeeeeeeeeeeeeeeedfssfsfs": [
        5,
        5,
        5,
        5,
        4,
        56,
        65,
        475,
        767,
        5,
        858,
        57,
        f["oooooooooooooooooooooooooooooooooooo"],
        f["ldflgkgkdotigksdsvmdlgvksmvlkgvm"],
        8,
        67,
        867,
    ],
}


def bfs(graph, source):
    queue = deque()
    queue.append(source)
    while len(queue) > 0:
        current = queue.popleft()
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)


bfs(graph, "a")
