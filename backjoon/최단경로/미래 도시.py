"""
이코테 p259

첫째쭐에 전체 회사 갯수 N과 경로의 개수 M이 공백으로 구분되어 차례로 주어짐
둘째줄부터 M+1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다
M+2번쨰 줄에는 X와 K가 공백으로 구분되어 차례로 주어진다.

1번에서 출발 X를 거쳐 K로 가야한다.
만약 X에 안가지면 -1출력한다.

"""

"""
N이 100 미만이므로 플로이드워셜로 풀어도 그리 오래 걸리지 않는다.

5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

-> 3

4 2
1 3
2 4
3 4


-> -1


"""

INF = int(1e9)
n, m = map(int, input().split())


graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    # a, b 서로 가는 비용은 1이라 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


x, k = map(int, input().split())

# 같은 위치에 있는 값은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)