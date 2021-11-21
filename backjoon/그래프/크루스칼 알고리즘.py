"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25


-> 159

크루스칼은 최소 비용부터 간선 하나씩 넣은 뒤 사이클이 돌면 그 간선은 빼는식으로 진행한다.

사이클 돈다는것을 어떻게 표현하지..
-> 서로소 집합 알고리즘에서 만든것을 이용해야한다.
"""
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b




# 노드 : v 간선 : e
v, e = map(int, input().split())

parent = [0] * (v+1) # 부모 테이블 초기화

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    c, a, b = edge

    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent, a,b)
        result += c

print(result)
