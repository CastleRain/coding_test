"""
https://www.acmicpc.net/problem/2178


0,0 -> n-1, m-1로 가면된다.

"""

from collections import deque



n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input())))

# 상 우 하 좌
dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if data[nx][ny] == 0:
                continue

            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx, ny))
    return data[n-1][m-1]
print(bfs(0, 0))
