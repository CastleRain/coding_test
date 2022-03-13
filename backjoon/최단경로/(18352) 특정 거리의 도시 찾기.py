"""
문제 링크 : https://www.acmicpc.net/problem/18352
푼 날짜 : 220313
문제 유형 : 최단거리


풀이 : 

단방향 도로

"""

import sys
import heapq
input = sys.stdin.readline

INF = 1e9

def solution(n,m,k,x):
    result = []
    distance = [INF] * (n+1) # 자기자신부터 n개의 도시까지 초기화
    
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b) # 단방향
    
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist: # 저장되어있는 값이 더 작은경우 pass
            continue
        elif distance[now] > k: # 현재 거리가 k보다 큰 경우 pass
            continue
            
        for i in graph[now]:
            heapq.heappush(q, (dist+1, i))
            distance[i] = min(distance[i], dist+1)

    for idx, val in enumerate(distance):
        if val == k:
            result.append(idx)

    return result

if __name__ == "__main__":
    n, m, k, x = map(int, input().split())

    result = solution(n,m,k,x)
    if len(result) ==0:
        print('-1')
    else:
        for i in sorted(result):
            print(i)