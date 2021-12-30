"""
https://www.acmicpc.net/problem/1260


"""
import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for i in range(m+1)]
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(graph, v, visited):
    
    dfs_visited[v] = True
    print(v, end = " ")
    for i in graph[v]:
        
        if not visited[i]:
            dfs(graph, i, visited)
    


dfs(graph, v, dfs_visited)
print()

queue = deque([v])


while len(queue):
    q = queue.popleft()
    if not bfs_visited[q]:
        
        print(q, end = " ")

        bfs_visited[q] = True

        for k in graph[v]:
            if not bfs_visited[k]:
                queue.append(k)
    


