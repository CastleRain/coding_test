"""
https://www.acmicpc.net/problem/12896

N개 도시 양방향
최소 비용, N-1개의 도로를 이용해서 모든 도시 사이 단 한개의 경로

하나의 도시에 소방서 건설

소방서는 최적의 위치

한 도시에서 다른 도시로 연결된 도로는 거리가 1


천나라에 있는 도시의 수, 도로의 연결 상태, 최적의 위치 설치된 소방서 -> 다른 도시에 도착할 때 이동하는 거리들 중 최대 거리


DFS? 최적의 거리 = 다익스트라? 워셜?
N = 100000

2억까지 커버가능

d[a].append(b)
d[b].append(a)

10만 N을 for에 넣게되면 최대 2000번의 연산만 할 수 있음


각 노드별 길이를 구한다 -> 10만

1   1
2   2
3   1
4   2
5   1


"""

import sys

input = sys.stdin.readline


def solution():
    return 0

if __name__ == "__main__":

    solution()