"""
6 4
1 4
2 3
2 4
5 6

-> 1 2 3 4
-> 5 6
이렇게 묶인다.

원하는 결과는 각 원소가 집한 집합과 부모 테이블이 어디인지 보여주는것이다.
(부모는 자신보다 낮은 숫자로 구성되어야한다.)

각 원소가 속한 집합 : 1 1 1 1 5 5
     부모 테이블   : 1 1 2 1 5 5

N과 M이 처음 들어오며 N은 노드의 갯수 M은 간선의 갯수이다.

"""


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])

    print(x)
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

# 노드 갯수만큼 리스트를 만든다.
parent = [0] * (n+1)

# 처음은 자기자신을 가르키도록 만든다.
for i in range(len(parent)):
    parent[i] = i

for i in range(m):
    a, b = map(int, input().split())
    # 현재 값에서 루트값 찾기 -> 현재 자신의 parent값이 자기자신이 될때까지 진행이 되어야한다.
    union_parent(parent, a, b)


print('각 원소가 속합 집합 : ', end = "")
for i in range(1, n+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블 : ', end = "")
for i in range(1, n+1):
    print(parent[i], end= " ")