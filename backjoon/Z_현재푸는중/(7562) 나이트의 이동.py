"""
문제 링크 : https://www.acmicpc.net/problem/7562
푼 날짜 : 220316
문제 유형 : dfs -> bfs!!!!!!!!!!!


풀이 : 
다시 풀어보자.

dfs가 아닌 bfs로 풀어야한다.

"""

import sys

def dfs(graph, x, y, e_x, e_y, cnt):
    global result
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1 ,-2 ]

    if x==e_x and y == e_y:
        result = min(result, cnt)
        return
        


    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위에 벋어나지 않고
        if 0<= nx <= len(graph)-1 and 0 <= ny <= len(graph)-1:
            if not graph[nx][ny]: # 방문하지 않은곳이라면
                graph[x][y] = True
                cnt += 1
                dfs(graph, nx, ny, e_x, e_y, cnt)
        # 벋어나면 pass

    return



def solution(size):
    global result

    graph = [[False] * size for _ in range(size)] # size * size사이즈의 그래프 생성

    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    graph[start_x][start_y] = True

    dfs(graph, start_x, start_y, end_x, end_y, 0)


    return result

if __name__ == "__main__":

    n = int(input())
    for _ in range(n):
        result = 1e9
        size = int(input())
        print(solution(size))


