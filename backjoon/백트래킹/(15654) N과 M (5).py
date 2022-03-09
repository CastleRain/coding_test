"""
https://www.acmicpc.net/problem/15652

중복허용
자기 자신을 받아오긴하나 자기보다 낮은숫자는 받아오면 안된다.


"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# data 받아와서 sort진행한다. 만약 데이터가 컸을 경우 heapq를 이용해서 바로 정렬해주자.
data = []
for d in list(map(int, input().split())):
    data.append(d)
data.sort()

result = []

visited = [False] * n

def n_m(result, visited, data):

    if len(result) == m:

        print(" ".join(result))
        return

    
    for i in range(n):
        if not visited[i]:

            visited[i] = True
            result.append(str(data[i]))

            n_m(result, visited, data)

            pop_data = result.pop()

            visited[data.index(int(pop_data))] = False

n_m(result, visited, data)