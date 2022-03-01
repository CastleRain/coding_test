"""
https://www.acmicpc.net/problem/1012

배추 근처에서 서식하며 해충을 잡아먹는다.
어떤 배추에 저링이가 한마리라도 살고있으면 이 지렁이는 인접한 다른 추로 이동할 수 있어서 그 배추도 보호가능

상하좌우 네 방향에 다른 배추가 위치한 경우 서로 인접

최소 배추흰지렁이 마리수를 구해라.

dfs를 사용하는 문제였다. 아직 문제를 보는 눈이 없구나..

"""
import sys

# 백준에서 RecursionError가 안나게한다.
sys.setrecursionlimit(10**6)


def dfs(x, y):

    # 범위를 벋어나면 나가도록 하자.
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 만약 지렁이가 있는곳이면 
    if data[x][y] == 1:
        
        # 방문했다는 의미로 0으로 돌려놓자.
        data[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        # 처음 들어온 값이므로 True로 리턴을 주자.
        return True
    
    return False

t = int(input())

for _ in range(t):

    m, n, k = map(int, input().split())

    data = [[0] * m for i in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        data[b][a] = 1
    
    result = 0
    for i in range(m):
        for j in range(n):

            # 처음 들어온 값에 대해서만 1을 더해준다.
            if data[j][i] == 1:
                dfs(j, i)
                result += 1

    print(result)




        






