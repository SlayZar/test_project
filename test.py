# unformatted code
import pandas as pd
from collections import deque
import numpy as np
from typing import List
from typing import Int


f = {
    "oooooooooooooooooooooooooooooooooooo": 123456,
    "ldflgkgkdotigksdsvmdlgvksmvlfvz dkjfvnzkjvznfjkdvnkfjdvnzfvfvfvzdfvzmkjvmkkgvm": 4356586586656858689596856596895896875863454554545,
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
