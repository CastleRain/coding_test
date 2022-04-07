"""
양 # .풀

## 붙어있다면 한무리의 양이 있다

첫번째 줄 -> 테스트 케이스 수 T
H : 그리드의 높이 
W : 그리드의 너비

"""
import sys

# 백준에서 RecursionError가 안나게한다.
sys.setrecursionlimit(10**6)
t = int(input())

def dfs(x, y, visited):

    visited[x][y] = True

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] == "#":
                dfs(nx, ny, visited)
    return

for _ in range(t):
    n, m = map(int, input().split())
    graph = []

    for _ in range(n):
        graph.append(list(map(str, input())))

    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == "#":
                cnt += 1
                dfs(i, j, visited)
    print(cnt)

    
