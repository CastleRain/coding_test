"""
도시분할 계획
https://www.acmicpc.net/problem/1647


1. 유지비 최소 (크루스칼 알고리즘)
2. 2개로 분리 -> 코스트가 젤 큰 도로 제거

첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2이상 100,000이하인 정수이고, M은 1이상 1,000,000이하인 정수이다.
그 다음 줄부터 M줄에 걸쳐 길의 정보가 A B C 세 개의 정수로 주어지는데 A번 집과 B번 집을 연결하는 길의 유지비가 C (1 ≤ C ≤ 1,000)라는 뜻이다.

7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

8
"""
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        # return find_parent(parent, parent[x])
    # return x
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

data = []
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    data.append((cost, a, b))

# cost를 기준으로 정리
data.sort()

# 서로소 알고리즘 진행
result = 0
last = 0


for i in data:
    cost, a, b = i

    # 만약 사이클을 돌지않는다면 union을 진행하고 cost를 추가한다.
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost


print(result - last)
