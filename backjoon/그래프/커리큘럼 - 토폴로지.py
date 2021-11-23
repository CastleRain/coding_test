"""
이코테 p303

선수 강의가있다.
ex) 알고리즘 강의의 선수강의로 자료구조와 컴퓨터 기초가 있다면 자료구조, 컴퓨터 기초를 모두 들은 후 알고리즘 강의를 들을수 있다.

총 N개의 강의를 듣고자 한다.
동시에 여러 강의를 들을수 있다.

첫번째 줄에 듣고자 하는 강의의 수 N(1 <= N <= 500)이 주어진다.,
다음 N개의 줄에는 강의의 시간과 강의를 듣기 위해서 먼저 들어야하는 강의들의 번호가 자연수로 주어진다.
각 강의번호는 1부터 N까지로 구성되며 각 줄은 -1로 끝난다


5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1


->
10
20
14
18
17


-> 토폴로지를 이용해서 풀어볼 예정이다.
"""

from collections import deque
import copy

# 노드의 개수 입력받기

v = int(input())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]
#각 강의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1:]:
        indegree[i] +=1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()
