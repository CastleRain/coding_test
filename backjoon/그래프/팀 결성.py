"""
이코테 p298

학생들에게 0번에서 N번까지 번호 부여하였다.
처음에는 다 다른팀으로 분류되어 N+1팀이 존재한다.

선생님은 1. 팀합치기, 2. 같은팀 여부확인 연산을 사용할 수 있다.
M개의 연산을 수행할 때 같은팀 여부 확인 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오

같은팀 여부확인은 1 a b로 나타낼수 있다.


7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1



-> No
No
YES


### 서로소 문제가 떠오른다. 그걸로 풀어보자

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


def check_parent(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        print("YES")
    else:
        print("NO")


# n : 학생수 m : 간선수
n, m = map(int, input().split())


parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i
for _ in range(m):

    check, a, b = map(int, input().split())

    # 팀 합치기 (제일 앞선 사람의 번호로 합친다.)
    if check == 0:
        union_parent(parent, a, b)
    # 같은팀 여부 확인
    else:
        check_parent(parent, a, b)