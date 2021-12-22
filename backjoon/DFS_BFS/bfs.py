"""

1. 일단 처음 들어오는 값에서 모든 값을 큐에 넣는다.
2. 큐를 pop을 진행하며 계속 집어넣는다.

"""

from collections import deque




def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True


    while queue:

        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

bfs(graph, 1, visited)

